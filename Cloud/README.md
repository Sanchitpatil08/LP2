# 💻 Google Cloud Engine Setup & Salesforce Apex Execution Guide

## Q2. 🚀 Google Cloud Engine Setup

### Step 1: Install Google Cloud SDK
- Visit the official install page: [https://cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install)
- Scroll to the **Windows** section and copy the installation command for **PowerShell**.
- Open **PowerShell as Administrator** and paste the command to install the SDK.

### Step 2: Initialize Google Cloud CLI
- After installation, log in using your Google Account.
- Run the following command in **Google Cloud SDK Shell**:
  ```bash
  gcloud projects create Riya-pract--project1 --set-as-default
  ```

### Step 3: Setup Project Files
- Go to: [https://github.com/sanchitpatil08/cloud/google-app-engine](https://github.com/sanchitpatil08/cloud/google-app-engine)
- Download the ZIP file and extract it to your **Desktop**.

### Step 4: Link Billing Account
- Go to: [https://console.cloud.google.com](https://console.cloud.google.com)
- Select your newly created project (`Riya-pract--project1`) from the top navbar.
- Navigate to the **Billing** section and link your billing account.

### Step 5: Deploy to Google App Engine
- Open **Google Cloud SDK Shell** from your Desktop.
- Navigate to your project folder:
  ```bash
  cd "C:\Users\<YourUsername>\Desktop\<ExtractedFolderName>"
  ```
- Deploy the app:
  ```bash
  gcloud app deploy
  ```
  - Press **Yes** when prompted and select **zone 7**.
  - If an error occurs, re-run the same deploy command.

### Step 6: View Your Deployed App
```bash
gcloud app browse
```

---

## Q3. 🔢 Salesforce Apex Class Setup

### Step 1: Login to Salesforce Developer Console
- Go to: [https://developer.salesforce.com](https://developer.salesforce.com)
- Log in to your account.

### Step 2: Create Apex Class
- Click the **Gear Icon (⚙️)** at the top-right and open **Developer Console**.
- Go to **File → New → Apex Class**.
- Name the class: `Calculator`

### Step 3: Paste the Following Code:
```apex
public class Calculator {

    // Addition
    public static Double add(Double a, Double b) {
        return a + b;
    }

    // Subtraction
    public static Double subtract(Double a, Double b) {
        return a - b;
    }

    // Multiplication
    public static Double multiply(Double a, Double b) {
        return a * b;
    }

    // Division with zero check
    public static Double divide(Double a, Double b) {
        if (b == 0) {
            System.debug('Cannot divide by zero');
            return null;
        }
        return a / b;
    }
}
```
- Click **Save** or press `Ctrl + S`.

### Step 4: Execute the Code
- Go to **Debug → Open Execute Anonymous Window**.
- Paste the following:
```apex
// Declare variables
Double num1 = 20;
Double num2 = 5;

// Perform calculations
Double sum = Calculator.add(num1, num2);
Double diff = Calculator.subtract(num1, num2);
Double product = Calculator.multiply(num1, num2);
Double quotient = Calculator.divide(num1, num2);

// Print results in debug log
System.debug('Addition Result: ' + sum);
System.debug('Subtraction Result: ' + diff);
System.debug('Multiplication Result: ' + product);
System.debug('Division Result: ' + quotient);
```
- Click **Execute**.

### Step 5: View Debug Logs
- Click the **Log** tab.
- Check the **Debug Only** checkbox to view only the debug output.

---

✅ You’ve successfully deployed a Google App Engine project and executed an Apex class in Salesforce!
