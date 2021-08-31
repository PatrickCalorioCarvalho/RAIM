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
  MVRAIM = getStatusService("MVRAIM")
  MFRAIM = getStatusService("MFRAIM")
  PDRAIM = getStatusService("PDRAIM")
  CHRAIM = getStatusService("CHRAIM")
  return render_template('index.html',Mysql=Mysql,MQTT=MQTT,MVRAIM=MVRAIM,MFRAIM=MFRAIM,PDRAIM=PDRAIM,CHRAIM=CHRAIM)

if __name__ == "__main__":
 app.run(host='0.0.0.0', port=5000)

