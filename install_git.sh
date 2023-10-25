sudo apt install git
sudo apt install python3
sudo apt install pip 
pip install psutil
sudo apt-get install -y systemd

git clone https://github.com/ArijAchour/code-
sudo cp test.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable test.service
sudo systemctl start test.service