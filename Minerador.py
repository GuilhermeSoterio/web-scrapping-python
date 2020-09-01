import json
import funcoes as fun
import os
import bot
from bs4 import BeautifulSoup

def minerar():

  linkPage = "http://www.ifb.edu.br/brasilia/noticiasbrasilia"
  respostaHttp = fun.getPage(linkPage)
  soup = BeautifulSoup(respostaHttp.read(), features="html.parser")

  capturaDataHora = fun.getDataHora(soup)
  capturaImg = fun.getImagem(soup)
  capturaTitulo = fun.getTitle(soup)
  capturaDescricao = fun.getDescricao(soup)
  capturaLink = fun.getUrlNoticia(soup)

  listaDataHora = []
  listaImg = []
  listaTitulo = []
  listaDescricao = []
  listaLinkNoticia = []

  if(capturaImg!=None and capturaTitulo!=None and capturaDescricao!=None and capturaLink!=None and capturaDataHora!=None):
    #variavel negrito
    iBold = "<b>"
    fBold = "</b>"
    #variavel italico
    iItalic = "<i>"
    fItalic = "</i>"

    for i in range(len(capturaTitulo)):
      listaDataHora.append(iItalic+capturaDataHora[i].strip()+fItalic)
      listaImg.append('<a href="{}{}">.</a>'.format("https://www.ifb.edu.br",capturaImg[i]))
      listaTitulo.append(iBold+capturaTitulo[i].get_text().strip()+fBold)
      listaDescricao.append(capturaDescricao[i].get_text().strip())
      listaLinkNoticia.append("https://www.ifb.edu.br{}".format(capturaLink[i]))

  else:
    print("Ocorreu um erro na captura das informações!")

  listaDeNoticias = {}

  for i in range(10): 
    listaDeNoticias[listaDataHora[i]] = \
    (
      listaTitulo[i],
      listaDescricao[i],
      listaImg[i],
      listaLinkNoticia[i]
    )

  nomeArquivoJson = "noticias.json"
  nomeArquivoTmp = 'arquivo.tmp'

  if (os.path.exists(nomeArquivoJson)):
    a = open(nomeArquivoJson, "r")
    noticiasJs = json.loads(a.read())
    a.close()

    ultimaDataHora = fun.getTmpData(nomeArquivoTmp)
    ultimaDataHora = fun.getData(ultimaDataHora)

    for dataHora in listaDeNoticias.keys():
      dataHoraConvertida = fun.getData(dataHora)

      if dataHoraConvertida > ultimaDataHora:
        noticiasJs[dataHora] = \
          (
            listaDeNoticias[dataHora][0],
            listaDeNoticias[dataHora][1],
            listaDeNoticias[dataHora][2],
            listaDeNoticias[dataHora][3]
          )
  
    a = open(nomeArquivoJson, 'w')
    js = json.dumps(noticiasJs, ensure_ascii=False, indent=2)
    js = str(js)
    a.write(js)
    a.close()
  else:
    js = json.dumps(listaDeNoticias, ensure_ascii=False, indent=2)
    js = str(js)
    a = open(nomeArquivoJson, 'w')
    a.write(js)
    a.close()

  arquivo_tmp = open(nomeArquivoTmp, 'w')
  arquivo_tmp.write(list(listaDeNoticias.keys())[0])
  arquivo_tmp.close()

if __name__ == "__main__":
  minerar()