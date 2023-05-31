<h1 align="center"> SmartSummy</h1>

![license](http://img.shields.io/static/v1?label=license&message=MIT&color=GREEN&style=for-the-badge)

# Índice 
* [Descrição do Projeto](#descrição-do-projeto)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Licença](#licença)
* [Conclusão](#conclusão)

## Descrição do Projeto
SmartSummy, é proposta nesse trabalho que utiliza modelos pré-treinados,
Whisper e LED para gerar resumos em português de vídeos em inglês. Com essa ferramenta, é possível
economizar tempo e facilitar o acesso a informações importantes, tornando o processo de aprendizado mais
eficiente.

A solução SmartSummy foi desenvolvida em Python, utilizando modelos pré-treinados para processamento
de áudio e texto. O processo é dividido em quatro fases. Na primeira fase, o áudio do vídeo
é extraído utilizando a biblioteca MoviePy. Em seguida, o áudio é processado pelo Whisper, O texto
gerado pelo Whisper é então repassado para o LED (Longformer-Encoder-Decoder). Por fim, o texto
resumido é traduzido para o português utilizando a biblioteca GoogleTrans.

Saiba mais sobre o Whisper em :https://github.com/openai/whisper.git

### Dependencias

! pip install git+https://github.com/openai/whisper.git

! pip install jiwer

! pip install transformers

! pip install googletrans==4.0.0-rc1

! pip install moviepy

! pip install python-ffmpeg

! pip3 install torch torchvision torchaudio



## Funcionalidades e Demonstração da Aplicação
Dentro do diretorio do projeto, podemos executa-lo da seguinte forma pelo prompt de comando:

```sh
python smartsummy.py videoplayback.mp4
```
O video de exemplo é o "How Modern Audiences Can Talk about Aging Art | Margaret Hall | TED" https://www.youtube.com/watch?v=uH9r3lJmyaM
com 10 min de duração. Exemplo de executação:

![image](https://github.com/Keomas/SmartSummy/assets/6170063/a1f1f2e9-bd5f-4207-beb4-93a256379603)

Texto do video resumido em português:

> O narrador se apresenta e explica o objetivo de sua palestra: ajudar as pessoas na platéia a entender como a arte está mudando.
> O teatro, ela diz, é uma "forma de arte colaborativa" e, portanto, deve ser capaz de se comunicar através da arte.
> A pergunta, ela pergunta, é "como abordamos a arte envelhecida?"O musical é relativamente jovem, ela explica, com suas seis gerações artísticas passadas desde o início.
> Segundo ela, isso significa que passou pelo "marcador antigo", assim como todas as outras formas de arte que a precederam.
> Ela usa a adaptação de Henry M. Grant em 1866 do melodrama de George Cruikshank, The Black Crow, para ilustrar o ponto de que não há marcadores para quando a arte deve ser vista como velha ou nova;Em vez disso, deve ser visto como parte de um diálogo contínuo e contínuo entre os seres humanos.

## Conclusão
Em conclusão, o SmartSummy é uma solução muito promissora para gerar resumos de vídeos em
inglês, tornando o processo de obtenção de informações mais rápido e eficiente. Utilizando modelos
pré-treinados como o Whisper e o LED, o SmartSummy foi capaz de produzir resumos de alta qualidade
para vídeos em inglês, com resultados satisfatórios em testes realizados com dois vídeos diferentes.
o o processo de pesquisa e estudo
mais ágil e eficiente.[SmartSummy.pdf](https://github.com/Keomas/SmartSummy/files/11617325/SmartSummy.pdf)

