import json
import pickle
import telebot


def tabla_json():
  ruta='media/equipos.json'
  with open(ruta) as f:
    equipos=json.load(f)
  
    #ordenar
    order=sorted(equipos['equipos'], key=lambda ganados: ganados['G'], reverse=True)

    # converitendo a String
    text = json.dumps(order, indent=4)
  return text   


# noticias

def news_json():
  ruta='media/noticias.json'
  txt=[]
  with open(ruta) as f:
    noticias=json.load(f)
    #for x in noticias['noticias']:
     # txt.append(x)
    text = json.dumps(noticias, indent=4, ensure_ascii=False)
    # converitendo a String
    
  return text   

news_json()

#resultados



def resultados():
  resultados=[]

  juego1="GRM 4-9 MTZ "
  juego2="STG 12-7 ART "
  juego3="GTM 5-4 PR "
  juego4="HOL 7-3 MAY "
  juego5="LTU 8-4 ISL "
  juego6="CMG 16-5 SSP "
  juego7="VCL 3-2 CFG "
  juego8="IND 3-6 CAV "
  
  resultados.append(juego1)
  resultados.append(juego2)
  resultados.append(juego3)
  resultados.append(juego4)
  resultados.append(juego5)
  resultados.append(juego6)
  resultados.append(juego7)
  resultados.append(juego8)

  return resultados

print(resultados())  

#bot
     


bot=telebot.TeleBot('6058279985:AAFcu82w8rfcAMvS0x9qQHS3dpJeUVj5goE', parse_mode=None)

@bot.message_handler(commands=['ayuda'])
def send_welcome(message):
	bot.reply_to(message, "Comandos\n /tabla posiciones de Equipos\n /noticias noticias\n /resultados resultados de la jornada\n /lb lideres de  Bateo\n /lp lideres de picheo\n /about Acerca de")
 

@bot.message_handler(commands=['/stop'])
def send_welcome(message):
	bot.stop_polling()
	
	






@bot.message_handler(commands=['tabla'])
def send_stat(message):
	photo = open('media/tabla.png', 'rb')
	bot.send_photo(message.chat.id, photo) 	
 
@bot.message_handler(commands=['noticias'])
def send_noticias(message):
	bot.send_message(message.chat.id, news_json()) 

@bot.message_handler(commands=['resultados'])
def send_resultados(message):
	txt='\n'.join(resultados())
	bot.send_message(message.chat.id, txt) 
 
@bot.message_handler(commands=['lb'])
def send_lb(message):
	photo = open('media/lb.png', 'rb')
	bot.send_photo(message.chat.id, photo) 
	
@bot.message_handler(commands=['lp'])
def send_lp(message):
	photo = open('media/lp.png', 'rb')
	bot.send_photo(message.chat.id, photo) 	

@bot.message_handler(commands=['about'])
def send_about(message):
	bot.send_message(message.chat.id, 'Grupo para dar informacion sobre la SNB\n Version: 1.00\n Actualizacion: 1/4/2023\n Creador: Carlos Garcia ') 

  


#arrancar el bot
bot.infinity_polling()

 
