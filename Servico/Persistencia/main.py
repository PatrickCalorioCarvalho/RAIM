import paho.mqtt.client as mqtt
import json
import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.18.249",
  user="pi",
  password="raspberry",
  database="RAIM"
)
def on_connect(client, userdata, flags, rc):
    print("OK")
    client.subscribe("raim/estacoes/#")

def on_message(client, userdata, msg):
    if(msg.retain == 0):
        Leitura = json.loads(msg.payload)
        IDEstacaoMeteorologica = int(msg.topic.split("/")[-1])
        Temperatura = float(Leitura['Temperatura'])
        Umidade = float(Leitura['Umidade'])
        Pressao = float(Leitura['Pressao'])
        sql = "insert into LeituraMeteorologica(IDEstacaoMeteorologica,Temperatura,Umidade,Pressao,DataLeitura) values(%s,%s,%s,%s,Now())"
        val = (IDEstacaoMeteorologica,Temperatura,Umidade,Pressao)
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()
        

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('192.168.18.249', 1883, 60)
client.loop_forever()
