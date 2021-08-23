# Configuração do Serviço De Monitoramento

1. Pré-requisito, executar comando para instalação do PIP
```bash
sudo apt-get install python3-pip
```

### Físico

![MonitoramentoFisico](./img/MonitoramentoFisico.gif)

1. Pré-requisito, executar comando para instalação de pacotes
```bash
sudo apt-get install python3-pil
sudo apt-get install python3-smbus
sudo apt-get install git
git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
cd Adafruit_Python_SSD1306
sudo python3 setup.py install
```

2. Execute o comando, para habilidar I2C
```bash
sudo raspi-config 
```
![RaspberryPiRaspiConfiI2C](./img/RaspberryPiRaspiConfiI2C.PNG)

3. Selecione a Opção Interface Options 

![RaspberryPiInterfaceOptionsI2C](./img/RaspberryPiInterfaceOptionsI2C.PNG)

4. Selecione a Opção I2C 

![RaspberryPiI2C](./img/RaspberryPiI2C.PNG)

5. Selecione a Opção "YES"
   
### Virtual

#### Web

![MonitoramentoVirtualWeb](./img/MonitoramentoVirtualWeb.PNG)

#### Mobile

![MonitoramentoVirtualMobile](./img/MonitoramentoVirtualMobile.jpeg)

1. Pré-requisito, executar comando para instalação de pacotes
 
```bash
sudo pip3 install flask
```