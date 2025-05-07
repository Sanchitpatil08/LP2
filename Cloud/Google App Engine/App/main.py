from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Simple Calculator</title>
    <style>
        body { font-family: Arial; background: #f2f2f2; text-align: center; padding-top: 50px; }
        .calculator { background: white; padding: 30px; display: inline-block; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.2); }
        input, select { padding: 10px; margin: 10px; font-size: 16px; }
        .result { font-size: 18px; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="calculator">
        <h2>Simple Calculator</h2>
        <form method="post">
            <input type="number" name="num1" placeholder="First Number" required step="any">
            <input type="number" name="num2" placeholder="Second Number" required step="any">
            <br>
            <select name="operation">
                <option value="add">Add (+)</option>
                <option value="subtract">Subtract (-)</option>
                <option value="multiply">Multiply (×)</option>
                <option value="divide">Divide (÷)</option>
            </select>
            <br>
            <input type="submit" value="Calculate">
        </form>

        {% if result is not none %}
            <div class="result">
                <strong>Result:</strong> {{ result }}
            </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = "Cannot divide by zero" if num2 == 0 else num1 / num2
        except Exception as e:
            result = f"Error: {e}"

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run()
