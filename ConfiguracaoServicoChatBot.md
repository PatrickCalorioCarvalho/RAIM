# Configuração do Serviço De ChatBot

1. Pré-requisito, executar comando para instalação do PIP
```bash
sudo pip3 install pandas
sudo pip3 install matplotlib
sudo pip3 install mysql-connector-python
sudo apt-get install libatlas-base-dev
sudo apt-get install libopenjp2-7
sudo pip3 uninstall numpy
sudo pip3 install  numpy
sudo pip3 install pyTelegramBotAPI
```


2. Criando Serviço ChatBotRAIM
```bash
cd /lib/systemd/system/
sudo nano CHRAIM.service
```

```bash
[Unit]
Description=ChatBotRAIM
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/pi/RAIM/Servico/ChatBot/main.py
Restart=on-abort

[Install]
WantedBy=multi-user.target
```

```bash
sudo chmod 644 /lib/systemd/system/CHRAIM.service
chmod +x /home/pi/RAIM/Servico/ChatBot/main.py
sudo systemctl daemon-reload
sudo systemctl enable CHRAIM
sudo systemctl start CHRAIM
```