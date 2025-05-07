
# ⚙️ Salesforce Apex Calculator – Setup & Execution Guide

This guide walks you through creating and executing a simple **Calculator class** using **Apex in Salesforce Developer Console**.

---

## 📋 Prerequisites

- A Salesforce Developer account  
  Sign up or log in at: [https://developer.salesforce.com](https://developer.salesforce.com)

---

## 🛠️ Step-by-Step Instructions

### 1. Log In and Open Developer Console

- Visit [Salesforce Developer](https://developer.salesforce.com)
- Log in to your Salesforce account
- Click the **Gear icon** (⚙️) on the top-right
- Select **Developer Console**

---

### 2. Create a New Apex Class

- Click on **File > New > Apex Class**
- Name the class `Calculator`
- Paste the following code:

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

- Save the file using **CTRL + S** or click **File > Save**

---

### 3. Execute Anonymous Code

- Go to **Debug > Open Execute Anonymous Window**
- Copy and paste the following code:

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

- Click **Execute**

---

### 4. View the Output

- After execution, go to the **Logs tab**
- Open the most recent log
- Check the **Debug Only** checkbox to filter and view the results:

```
Addition Result: 25.0
Subtraction Result: 15.0
Multiplication Result: 100.0
Division Result: 4.0
```

---

## ✅ Success!

You’ve successfully created and executed a simple **Calculator** using Apex on Salesforce.

---

## 💬 Author

[Sanchit Patil](https://github.com/sanchitpatil08)
