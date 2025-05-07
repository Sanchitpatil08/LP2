
# ☁️ Deploying a Web App using Google Cloud Engine

This guide helps you deploy a web application on **Google Cloud Platform (GCP)** using **Google App Engine** with the Cloud SDK on Windows.

---

## 📋 Prerequisites

- A Google account
- Access to a billing account on GCP
- Windows OS with Administrator access

---

## 🛠️ Step-by-Step Instructions

### 1. Download and Install Google Cloud SDK

Open **Windows PowerShell as Administrator** and run the following command:

```powershell
(New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")
& $env:Temp\GoogleCloudSDKInstaller.exe
```

---

### 2. Login and Setup CLI

Once installation is complete:

- Launch **Google Cloud SDK Shell** from your desktop.
- Login using your Google account.
- Create and set a default project by running:

```bash
gcloud projects create Riya-pract--project1 --set-as-default
```

---

### 3. Download the Application Code

1. Visit the GitHub repository:
   [https://github.com/sanchitpatil08/cloud/google-app-engine](https://github.com/sanchitpatil08/cloud/google-app-engine)
2. Download the ZIP file.
3. Extract it to your desktop.

---

### 4. Link Billing Account

- Go to [Google Cloud Console](https://console.cloud.google.com)
- Open the **Navigation Menu** > **Projects**
- Select the project you just created (`Riya-pract--project1`)
- Go to **Billing** and link your billing account to this project.

---

### 5. Deploy the Application

1. Open **Google Cloud SDK Shell**
2. Navigate to your project folder:

```bash
cd "C:\Users\<YourUsername>\Desktop\<ExtractedFolderName>"
```

3. Deploy the app:

```bash
gcloud app deploy
```

> During the deployment, type `Y` for yes and select a region (preferably region **7**).

If an error occurs, simply re-run the command:

```bash
gcloud app deploy
```

---

### 6. Browse Your Application

After successful deployment, open the application in the browser:

```bash
gcloud app browse
```

---

## ✅ Your App is Live on Google Cloud!

Congratulations! Your app is now deployed on **Google App Engine**.

---

## 💬 Author

[Sanchit Patil](https://github.com/sanchitpatil08)
