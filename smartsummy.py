# -*- coding: utf-8 -*-

import whisper
import torch
from transformers import pipeline
import extract_audio_video
from googletrans import Translator
import sys
import os



def whisper_get_text(path:str) -> str:
  print("path: "+path)
  model = whisper.load_model("base.en")

  audio = whisper.load_audio(path)

  result = model.transcribe(audio)
  return str(result["text"])

def summarizing(text:str) -> str:
  hf_name = 'pszemraj/led-large-book-summary'

  summarizer = pipeline("summarization", hf_name, device=0 if torch.cuda.is_available() else -1,)
  wall_of_text = text
  result = summarizer(
      wall_of_text,
      min_length=16,
      max_length=256,
      no_repeat_ngram_size=3,
      encoder_no_repeat_ngram_size=3,
      repetition_penalty=3.5,
      num_beams=4,
      early_stopping=True,)
  print(result)
  return result[0]['summary_text']

def translate_pt(text:str) -> str:
  translator = Translator(service_urls=['translate.google.com','translate.google.com.br'])
  translated = translator.translate(text, src='en',dest='pt')
  return translated.text

def main():
  print("###Extracting audio from "+sys.argv[1]+" ####")
  path=str(sys.argv[1]).strip()
  
  extract_audio_video.extract_audio(path)
  print("###Passing audio to whisper###")
  res = os.path.join(os.getcwd(), 'audio.mp3')

  text_exrtacted=whisper_get_text(res)

  print("####Summarizing with led-large-model")
  text_summarized=summarizing(text_exrtacted)

  print("Translate to Pt")

  text_final = translate_pt(text_summarized)
  print("Result :"+text_final)

if __name__ == "__main__":
    main()
