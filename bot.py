
import telepot
import json
import funcoes as fun
import time
import os

bot = telepot.Bot("621015027:AAHARD9PB0YBkvc4kIrAOo0V2777FjlNqjo")
chat_id = -391286650

def mandaNoticia(arquivo):
  cont=0
  repeat = 0

  if (os.path.exists("noticias.json")):
    arquivoTmpEnviado = "dataUltimaMsgEnviada.tmp" 
    a = open('noticias.json', 'r')
    noticias = json.loads(a.read())
    a.close()

    chaves = sorted(noticias.keys())

    iSep = ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"

    if(os.path.exists(arquivoTmpEnviado)):
      dtUltimaMsgEnviada = fun.getTmpData(arquivoTmpEnviado)
      jsDtUltimaMsgEnviada = dtUltimaMsgEnviada
      dtUltimaMsgEnviada = fun.getData(dtUltimaMsgEnviada)

      a = open(arquivoTmpEnviado,'w')
      a.write(str(jsDtUltimaMsgEnviada))
      a.close()

      for i in range(len(chaves)):
        dateTimeChavesAtual = fun.getData(str(chaves[i]))
        if(dateTimeChavesAtual > dtUltimaMsgEnviada):
          cont=cont+1
          noticia = "{0}\n{1}\n{2}\n\n{3}{4}\n\n{5}".format(
            iSep,
            noticias[chaves[i]][0],
            chaves[i], 
            noticias[chaves[i]][1], 
            noticias[chaves[i]][2], 
            noticias[chaves[i]][3])
          
          bot.sendMessage(chat_id, noticia,parse_mode="HTML")
          time.sleep(2)
        elif(cont==0 and repeat==0):
          repeat=repeat+1
          print("::::::::Não existe novas mensagens:::::::::")
    else:
      while chaves!=[]:
        noticia = "{0}\n{1}\n{2}\n\n{3}{4}\n\n{5}".format(
          iSep,
          noticias[chaves[0]][0],
          chaves[0], 
          noticias[chaves[0]][1], 
          noticias[chaves[0]][2], 
          noticias[chaves[0]][3])
        
        dtUltimaMsgEnviada = chaves[0]
        del noticias[chaves[0]]
        del(chaves[0])

        bot.sendMessage(chat_id, noticia,parse_mode="HTML")
        time.sleep(2)

        a = open(arquivoTmpEnviado,'w')
        a.write(str(dtUltimaMsgEnviada))
        a.close()

    os.remove("noticias.json")
    print("O Arquivo foi deletado.")

    # a = open(arquivoTmpEnviado,'w')
    # a.write(str(dtUltimaMsgEnviada))
    # a.close()

  else:
    print("Não existe conteúdo no arquivo. Precisa minerar primeiro.")

if __name__ == "__main__":
  mandaNoticia("noticias.json")