import mysql.connector
import pandas as pd 
import matplotlib.pyplot as plt
import telebot
import time

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Veja Ultimas Leituras /photo")

@bot.message_handler(commands=['photo'])
def send_photo(message):
    mydb = mysql.connector.connect(
      host="192.168.18.249",
      user="pi",
      password="raspberry",
      database="RAIM"
    )
    sql = "SELECT Temperatura,Umidade,Pressao FROM LeituraMeteorologica"
    DFLeituraMeteorologica = pd.read_sql(sql, mydb)
    DFLeituraMeteorologica.plot(title='LeituraMeteorologica')
    nomePhoto = ("myplot"+str(time.time())+".png")
    plt.savefig(nomePhoto)
    bot.send_chat_action(message.chat.id, 'upload_photo')
    img = open(nomePhoto, 'rb')
    bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
    img.close()
    mydb.close()

bot.polling()

while True:
    time.sleep(0)