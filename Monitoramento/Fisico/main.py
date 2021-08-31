import time
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

RST = 24
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

def getStatusService(name):
    status = os.system("systemctl is-active --quiet "+name)
    if(status == 0):
        return "ON"
    else:
        return "OFF"

def EscreveInformacaoDisplayOLED(TituloInformacao,Informacao,draw,width,height):
    global image
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    font_titulo = ImageFont.truetype('/home/pi/RAIM/Monitoramento/Fisico/advanced_pixel_lcd-7.ttf', 8)
    font_info = ImageFont.truetype('/home/pi/RAIM/Monitoramento/Fisico/advanced_pixel_lcd-7.ttf', 16)
    top = 10
    draw.text((0, top), TituloInformacao, font=font_titulo, fill=255)
    draw.text((0, top+40), Informacao, font=font_info, fill=255)
    disp.image(image)
    disp.display()
    return


def MQTT(draw, width, height):
    EscreveInformacaoDisplayOLED("Serviço MQTT",getStatusService("mosquitto"),draw,width,height)
    return


def MYSQL(draw, width, height):
    EscreveInformacaoDisplayOLED("Serviço MYSQL",getStatusService("mariadb"),draw,width,height)
    return

def MonitoramentoVirtualRAIM(draw, width, height):
    EscreveInformacaoDisplayOLED("Serviço MVRAIM",getStatusService("MVRAIM"),draw,width,height)
    return

def MonitoramentoFisicoRAIM(draw, width, height):
    EscreveInformacaoDisplayOLED("Serviço MFRAIM",getStatusService("MFRAIM"),draw,width,height)
    return

def PersistenciaDadosRAIM(draw, width, height):
    EscreveInformacaoDisplayOLED("Serviço PDRAIM",getStatusService("PDRAIM"),draw,width,height)
    return    

def ChatBotRAIM(draw, width, height):
    EscreveInformacaoDisplayOLED("Serviço CHRAIM",getStatusService("CHRAIM"),draw,width,height)
    return

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height


image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

while True:
    MQTT(draw,width,height)
    time.sleep(3)
    MQTT(draw,width,height)
    time.sleep(3)
    MonitoramentoVirtualRAIM(draw,width,height)
    time.sleep(3)
    MonitoramentoFisicoRAIM(draw,width,height)
    time.sleep(3)
    PersistenciaDadosRAIM(draw,width,height)
    time.sleep(3)
    ChatBotRAIM(draw,width,height)
    time.sleep(3)