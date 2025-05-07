
# 🚀 Deploying Chat App on AWS EC2

This guide walks you through deploying your **Chat Application** on an Amazon EC2 instance using Amazon Linux and Node.js.

---

## 📋 Prerequisites

- An active [AWS Account](https://aws.amazon.com/)
- A basic understanding of AWS EC2
- SSH client (e.g., Terminal, Git Bash, or PuTTY)

---

## 🛠️ Deployment Steps

### 1. Login to AWS Console

Go to [AWS Console](https://console.aws.amazon.com/) and log in with your credentials.

---

### 2. Launch an EC2 Instance

- Navigate to **EC2 Dashboard**
- Click **Launch Instance**
- Set a name (e.g., `ChatAppServer`)
- Choose **Amazon Linux 2 AMI**
- Select an instance type (e.g., `t2.micro`)
- Create or select a key pair (used for SSH)
- Under **Security Group** settings, allow:
  - **SSH (port 22)**
  - **Custom TCP Rule (port 9001)** – Anywhere (0.0.0.0/0)
- Launch the instance

---

### 3. Connect to the EC2 Instance


### 4. Install Node.js and Git

Run the following commands:

```bash
sudo yum update -y
curl -sL https://rpm.nodesource.com/setup_18.x | sudo bash -
sudo yum install -y nodejs git
```

---

### 5. Clone the Chat App Repository

```bash
git clone https://github.com/sanchitpatil08/Chat-App
cd Chat-App
```

---

### 6. Install Dependencies

```bash
npm install
```

---

### 7. Start the Chat App

```bash
node index.js
```

> The app will start on **port 9001**.

---

### 8. Configure Inbound Rules (if not done earlier)

Go to your EC2 **Security Groups**:
- Click **Edit Inbound Rules**
- Add a new rule:
  - Type: **Custom TCP**
  - Port: **9001**
  - Source: **Anywhere (0.0.0.0/0)**

Save the changes.

---

### 9. Access the Application

- Open your browser
- Visit: `http://<your-ec2-public-ip>:9001`
- Open in **two tabs or two devices** to test the real-time chat

---

## ✅ Chat Application is Live!

Your real-time chat app is now successfully deployed on AWS EC2 and accessible over the internet.

---

### 10. If Already Deployed Code on instane 
 - Restart the instance
 - Connect to the instance
 - Run these Commands
 - ```bash
   cd Chat-App
   node index.js
```
- Your chat app is live on Port 9001




## 💬 Author

[Sanchit Patil](https://github.com/sanchitpatil08)
