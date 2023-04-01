import json
import pickle
import telebot


def tabla_json():
  ruta='media/equipos.json'
  with open(ruta) as f:
    equipos=json.load(f)
  
    #ordenar
    order=sorted(equipos['equipos'], key=lambda student: student['G'], reverse=True)

    # converitendo a String
    text = json.dumps(order, indent=4)
  return text   



def stats():
  equipos={}
  equipos['equipos']=[]
  

  granma={'nombre':'Granma', 'G':"4",'P':'0','Prom':'1.000','u10':'1-0','racha':' G-1'}
  guantanamo={'nombre':'Guantanamo', 'G':"1",'P':'0','Prom':'1.000','u10':'1-0','racha':' G-1'}
  santiago={'nombre':'Santiago de Cuba', 'G':"5",'P':'0','Prom':'1.000','u10':'1-0','racha':' G-1'}
  holguin={'nombre':'Holguin', 'G':"1",'P':'0','Prom':'1.000','u10':'1-0','racha':' G-1'}
  lastuna={'nombre':'Las tunas', 'G':"1",'P':'0','Prom':'1.000','u10':'1-0','racha':' G-1'}
  camaguey={'nombre':'Camaguey', 'G':"1",'P':'0','Prom':'1.000','u10':'1-0','racha':' G-1'}
  ciego={'nombre':'Ciego', 'G':"1",'P':'0','Prom':'1.000','u10':'1-0','racha':' G-1'}
  villa={'nombre':'Villa Clara', 'G':"1",'P':'0','Prom':'1.000','u10':'1-0','racha':' G-1'}
  ssp={'nombre':'Santi Spritu', 'G':"1",'P':'0','Prom':'1.000','u10':'1-0','racha':' G-1'}
  cienfuego={'nombre':'Cienfuego', 'G':"1",'P':'0','Prom':'1.000','u10':'1-0','racha':' G-1'}
  mtz={'nombre':'Matanza', 'G':"1",'P':'0','Prom':'1.000','u10':'1-0','racha':' G-1'}
  mayabeque={'nombre':'Mayabeque', 'G':"1",'P':'0','Prom':'1.000','u10':'1-0','racha':' G-1'}
  habana={'nombre':'Habana', 'G':"1",'P':'0','Prom':'1.000','u10':'1-0','racha':' G-1'}
  artemisa={'nombre':'Artemisa', 'G':"1",'P':'0','Prom':'1.000','u10':'1-0','racha':' G-1'}
  pinar={'nombre':'Pinar del Rio', 'G':"1",'P':'0','Prom':'1.000','u10':'1-0','racha':' G-1'}
  isla={'nombre':'Isla de la Juventud', 'G':"1",'P':'0','Prom':'1.000','u10':'1-0','racha':' G-1'}

  equipos['equipos'].append(granma)
  equipos['equipos'].append(guantanamo)
  equipos['equipos'].append(santiago)
  equipos['equipos'].append(holguin)
  equipos['equipos'].append(lastuna)

  equipos['equipos'].append(camaguey)
  equipos['equipos'].append(ciego)
  equipos['equipos'].append(villa)
  equipos['equipos'].append(ssp)
  equipos['equipos'].append(cienfuego)

  equipos['equipos'].append(mtz)
  equipos['equipos'].append(mayabeque)
  equipos['equipos'].append(habana)
  equipos['equipos'].append(artemisa)
  equipos['equipos'].append(pinar)
  equipos['equipos'].append(isla)

  with open('media/equipos.json','w') as f:
    json.dump(equipos,f)

#stats()

# noticias

def noticia_json():
  noticias={}
  noticias['noticias']=[]
  txt=[]
  news1={'noticia':'La Habana.- EN UNA maratonica jornada de 16 juegos a siete innings, Villa Clara mostró la nota más alta al ganar sus dos partidos contra Cienfuegos y quedarse como unico conjunto con tres triunfos sucesivos en la recién iniciada 62 Serie Nacional de Beisbol. A primera hora, en el estadio Augusto César Sandino, el equipo naranja vencio 4x3 con destaque ofensivo para su joven torpedero Christian Rodriguez (4-3). Abrio el derecho Freddy Asiel Alvarez, quien apenas admitio tres jits en cinco entradas y dejo el cotejo igualado 1x1. Gano el relevista Randy Cueto, autor de cuatro entradas a ritmo de dos sencillos. En el duelo de cierre los villaclareños se impusieron 7x5 tambien con destaque madero en ristre para el parador en corto Rodríguez, quien conectó de 3-3 con un triple y tres carreras impulsadas.'}
  news2={'noticia':'La FCB exigira derechos en caso de pitcher Yariel Rodríguez. La FCB requerira la cifra de 10 millones de dolares por daños y perjuicios.'}
  
  noticias['noticias'].append(news1)
  noticias['noticias'].append(news2)
 # txt.append('noticia--\n '+news['text'])
  
  with open('media/noticias.json','w') as f:
    json.dump(noticias,f)

#noticia_json()

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

  juego1="GRM 4-0 MTZ "
  juego2="STG 2-0 ART "
  juego3="GTM 3-5 PR "
  juego4="HOL 1-0 MAY "
  juego5="LTU 4-0 ISL "
  juego6="CMG 4-0 SSP "
  juego7="VCL 8-1 CFG "
  juego8="IND 4-0 CAV "
  
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
     


bot=telebot.TeleBot('6058279985:AAEuX1mCmt3Pd7wK46NDdQdt7ghOhamx9rI', parse_mode=None)

@bot.message_handler(commands=['ayuda'])
def send_welcome(message):
	bot.reply_to(message, "Comandos\n /tabla posiciones de Equipos\n /noticias noticias\n /resultados resultados de la jornada\n /lb lideres de  Bateo\n /lp lideres de picheo\n /about Acerca de")
 





@bot.message_handler(commands=['tabla'])
def send_stat(message):
	bot.send_message(message.chat.id, tabla_json()) 
 
@bot.message_handler(commands=['noticias'])
def send_welcome(message):
	bot.send_message(message.chat.id, news_json()) 

@bot.message_handler(commands=['resultados'])
def send_welcome(message):
	txt='\n'.join(resultados())
	bot.send_message(message.chat.id, txt) 
 
@bot.message_handler(commands=['lb'])
def send_welcome(message):
	photo = open('media/lb.png', 'rb')
	bot.send_photo(message.chat.id, photo) 

@bot.message_handler(commands=['about'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'Grupo para dar informacion sobre la SNB\n Version: 1.00\n Creador: Carlos Garcia ') 

  


#arrancar el bot
bot.infinity_polling()

 
