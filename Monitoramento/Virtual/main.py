from flask import Flask, render_template
import os
app = Flask(__name__)

def getStatusService(name):
  status = os.system("systemctl is-active --quiet "+name)
  if(status == 0):
    return "ON"
  else:
    return "OFF"


@app.route("/")
def index():
  Mysql = getStatusService("mariadb")
  MQTT = getStatusService("mosquitto")
  RAIMPersistencia = getStatusService("RAIMPersistencia")
  return render_template('index.html',Mysql=Mysql,MQTT=MQTT,RAIMPersistencia=RAIMPersistencia)

if __name__ == "__main__":
 app.run(host='0.0.0.0', port=5000)
