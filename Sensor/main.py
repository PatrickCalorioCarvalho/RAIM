import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
import BME280
from machine import Pin, I2C

esp.osdebug(None)
import gc
gc.collect()

ssid = 'Carvalho'
password = 'coxinha2021'
mqtt_server = '192.168.18.249'

client_id = ubinascii.hexlify(machine.unique_id())
topic_pub = b'raim/estacoes/1'

last_message = 0
message_interval = 5
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
  pass
print('Connection successful')

#i2c = I2C(1,scl=Pin(22), sda=Pin(21), freq=10000)
#bme = BME280.BME280(i2c=i2c)

def connect_mqtt():
  global client_id, mqtt_server
  client = MQTTClient(client_id, mqtt_server)
  client.connect()
  print('Connected to %s MQTT broker' % (mqtt_server))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

def read_bme_sensor():
  try:
    temp = b'%s' % bme.temperature[:-1]
    hum = b'%s' % bme.humidity[:-1]
    pres = b'%s'% bme.pressure[:-3]
    return temp, hum, pres
  except OSError as e:
    return('Failed to read sensor.')

try:
  client = connect_mqtt()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    if (time.time() - last_message) > message_interval:
      temp, hum, pres = read_bme_sensor()
      client.publish(topic_pub, "{""Temperatura"":"+temp+",""Umidade"":"+hum+",""Pressao"":"+pres+"}")
      last_message = time.time()
  except OSError as e:
    restart_and_reconnect()
