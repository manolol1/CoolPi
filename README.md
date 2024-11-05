Example Systemd service file:
```                                                           
[Unit]
Description=Python script for controlling a fan on a Rasberry Pi
After=network.target

[Service]
Type=idle
Restart=on-failure
User=pi
WorkingDirectory=/home/pi/CoolPi
ExecStart=/usr/bin/python /home/pi/CoolPi/cooling.py

[Install]
WantedBy=multi-user.target

```
