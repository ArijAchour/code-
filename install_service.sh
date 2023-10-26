cd /home/arij/code-
sudo cp monitoring_alert.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable monitoring_alert.service
sudo systemctl start monitoring_alert.service