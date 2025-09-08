🗳️ Voting App — Python Flask | Docker | Kubernetes | Linux Hosting
A simple Python Flask voting app with:
✅ Clean HTML UI
✅ Admin Login for Vote Reset
✅ Dockerized Deployment
✅ Kubernetes-ready manifests
✅ Linux hosting instructions (EC2/Ubuntu/CentOS)
📦 Quickstart: Run Locally
📥 Clone the Repoally
git clone https://github.com/atulkamble/voting-app.git
cd voting-app
🐍 Install Dependencies
python3 --version
pip3 --version
Install required Python packages:
pip3 install -r requirements.txt
🏃 Run the App
python3 app.py
Visit: http://127.0.0.1:5000
🎨 UI Features
📊 Live vote count with Chart.js bar graph

🔒 Admin login to reset votes

🖥️ Clean, mobile-friendly HTML interface

👨‍💻 Hardcoded admin credentials:

Username: admin
Password: admin
📁 Project Structure
voting-app/
├── app.py
├── Dockerfile
├── requirements.txt
├── templates/
│   ├── index.html
│   └── login.html
├── voting-app-deployment.yaml
└── voting-app-service.yaml
🐳 Run with Docker
🛠️ Build Docker Image
docker build -t atuljkamble/voting-app:latest .
📤 Push to Docker Hub
docker push atuljkamble/voting-app:latest
☸️ Deploy on Kubernetes
📦 Apply Deployment & Service
kubectl apply -f voting-app-deployment.yaml
kubectl apply -f voting-app-service.yaml
🌐 Get Service URL
kubectl get svc
On Minikube:

minikube service voting-app-service
📦 Linux Server (EC2/Ubuntu/CentOS) Hosting
1️⃣ Install Dependencies
Ubuntu:
sudo apt update -y
sudo apt install python3 python3-pip python3-venv git -y
RHEL/CentOS:
sudo yum install python3 python3-pip git -y
sudo pip3 install flask
2️⃣ Clone & Set Up App
git clone https://github.com/atulkamble/voting-app.git
cd voting-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3️⃣ Run App
python3 app.py
4️⃣ Open Firewall Port (if needed)
Ubuntu:

sudo ufw allow 5000/tcp
RHEL/CentOS:

sudo firewall-cmd --add-port=5000/tcp --permanent
sudo firewall-cmd --reload
5️⃣ Access App
Open: http://<server-ip>:5000

🔄 Run as a Background Service
nohup python3 app.py > app.log 2>&1 &
🎛️ Serve via Nginx on Port 80 (Optional)
Install Nginx
sudo apt install nginx -y
Add Reverse Proxy Config
sudo nano /etc/nginx/sites-available/voting-app
Contents:

server {
    listen 80;
    server_name <server-ip>;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
Enable config:

sudo ln -s /etc/nginx/sites-available/voting-app /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
Access at: http://<server-ip>

docker compose
docker-compose up -d
docker-compose down



ec2-amazon linux
sudo apt install python3 -y
sudo apt install python3-pip -y
sudo yum install git -y 
git --version
git config --global user.name "pradip pachapole"
git config --global user.email "pachapolp2932002@gmail.com "
git config --list 
git clone  https://github.com/PradipPach/voting-app.git
cd voting-app
pip3 install -r requirements.txt
python3 app.py 


ubuntu
sudo apt update -y 
sudo apt install tree -y 
sudo apt install python-is-python3
sudo apt update -y
sudo apt install python3-pip -y
sudo apt install git -y
git clone https://github.com/atulkamble/voting-app.git
cd voting-app/
sudo pip3 install flask 
sudo apt install python3.12-venv -y
sudo apt install pipx -y 
python3 -m venv venv
source venv/bin/activate 
pip install flask -y 
python app.py 


