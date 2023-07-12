from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Добро пожаловать!'

@app.route('/about')
def about():
    return 'О нас'

@app.route('/pic')
def picure():
    return render_template('picture.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Обработка данных формы, например, отправка электронной почты
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Здесь можешь добавить свою логику обработки данных формы

        return 'Спасибо за отправку формы!'
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(port=5001)
