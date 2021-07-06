import requests
import schedule
import time
import os
import telegram

bot = telegram.Bot('bot_token')

def rec():
	print('go rec.')
	t = time.time() + 10800
	stream_url = 'http://62.80.190.246:8000/ProstoRadiO128'
	r = requests.get(stream_url, 		stream=True)
	with open('stream.mp3', 'wb') as f:
      	  for block in r.iter_content(1024):
         	   f.write(block)
         	   if time.time() > t:
         	   	break
	
	#print(os.path.abspath(__file__))  
	bot.send_audio(chat_id=123456789, audio=open('stream.mp3', 'rb'))    
	print('send one...') 


schedule.every().day.at("05:00").do(rec)
schedule.every().day.at("10:00").do(rec)

while True:
    schedule.run_pending()
    time.sleep(1) 

