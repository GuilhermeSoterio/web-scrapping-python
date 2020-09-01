
import mineradorDeNoticias as minerador
import bot
import os

#--limpa o prompt de comando
# clear= lambda: os.system('cls')
clear= lambda: os.system('clear')
clear()

op = int(input("1 = Minerar \n2 = Bot\n"))
if op == 1:
  minerador.minerar()
elif op == 2:
  bot.mandaNoticia('noticias.json')
else:
  print("Opção inválida")