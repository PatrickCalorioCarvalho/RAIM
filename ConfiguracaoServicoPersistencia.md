# Configuração do Serviço De Persistência

1. Pré-requisito, executar comando para instalação do PIP
```bash
sudo pip3 install paho-mqtt
sudo pip3 install mysql-connector-python
```

2. Criando Serviço PersistenciaDadosRAIM
```bash
cd /lib/systemd/system/
sudo nano PDRAIM.service
```

```bash
[Unit]
Description=PersistenciaDadosRAIM
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/pi/RAIM/Servico/Persistencia/main.py
Restart=on-abort

[Install]
WantedBy=multi-user.target
```

```bash
sudo chmod 644 /lib/systemd/system/PDRAIM.service
chmod +x /home/pi/RAIM/Servico/Persistencia/main.py
sudo systemctl daemon-reload
sudo systemctl enable PDRAIM
sudo systemctl start PDRAIM
```