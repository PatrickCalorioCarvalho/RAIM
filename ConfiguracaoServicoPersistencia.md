# Configuração do Serviço De Persistência

1. Pré-requisito, executar comando para instalação do PIP
```bash
sudo pip3 install paho-mqtt
sudo pip3 install mysql-connector-python
```

2. Criando Serviço RAIMPersistencia
```bash
cd /lib/systemd/system/
sudo nano RAIMPersistencia.service
```

```bash
[Unit]
Description=RAIMPersistencia
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/pi/Servico/Persistencia/main.py
Restart=on-abort

[Install]
WantedBy=multi-user.target
```

```bash
sudo chmod 644 /lib/systemd/system/RAIMPersistencia.service
chmod +x /home/pi/Servico/Persistencia/main.py
sudo systemctl daemon-reload
sudo systemctl enable RAIMPersistencia
sudo systemctl start RAIMPersistencia
```