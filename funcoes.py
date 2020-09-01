from urllib.request import urlopen
from urllib.error import HTTPError
import datetime

def getPage(url):
  try:
    resposta = urlopen(url)
  except HTTPError as e:
    return None
  return resposta

def getTitle(soup):
  title = soup.body.findAll("h2", {"class":"tileHeadline"})
  return title

def getImagem(soup):
  imagem = []
  lista = soup.findAll("div", {"class":"tileItem"})
  for item in lista:
    if item.findAll("img"):
      imagem.append(item.findAll('img')[0].attrs['src'])
    else:
      imagem.append("/images/IFBVertical.png")
  return imagem

def getDescricao(soup):
  info = soup.body.findAll("span", {"class":"description"})
  return info

def getDataHora(soup):
  horario = []
  lista = soup.body.findAll("div", {"class":"span2 tileInfo"})
  for item in lista:
    horario.append(item.findAll('li'))
  for i in range(0, len(horario)):
    horario[i] = "{0} {1}".format(horario[i][2].get_text(), horario[i][3].get_text())
  return horario

def getTmpData(a):
  try:
    arq = open(a, 'r')    
    return arq.read()
  except:
    print("Erro na leitura do arquivo tmp.")

def getUrlNoticia(soup):
  link = []
  lista = soup.body.findAll("h2", {"class":"tileHeadline"})
  for item in lista:
    link.append(item.find('a').attrs['href'])
  return link

def getData(string):
  string = string.replace("<i>","").replace("</i>","")
  listaDeDados = string.split()
  ld = listaDeDados[0].split('/')
  listaDeHora = listaDeDados[1].split('h')
  ld.extend(listaDeHora)
  ld = list(map(int, ld))
  dt = datetime.datetime(2000+ld[2],ld[1],ld[0],ld[3],ld[4])
  return dt