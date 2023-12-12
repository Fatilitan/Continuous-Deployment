from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['bewerking']

        if operation == 'optellen':
            result = num1 + num2
        elif operation == 'aftrekken':
            result = num1 - num2
        elif operation == 'vermenigvuldigen':
            result = num1 * num2
        elif operation == 'delen':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Je kan niet delen door 0!"
        else:
            return "Kan niet"

        return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)