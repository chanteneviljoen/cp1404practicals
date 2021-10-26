from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=''):
    return f'Hello {name}'


@app.route('/f')
@app.route('/f/<celsius>')
def convert_to_fahrenheit(celsius=0):
    result = str(convert_celsius_to_fahrenheit(float(celsius)))
    return f'{celsius} degrees C is {result} degrees F'


@app.route('/c')
@app.route('/c/<fahrenheit>')
def convert_to_celsius(fahrenheit=0):
    result = str(convert_fahrenheit_to_celsius(float(fahrenheit)))
    return f'{fahrenheit} degrees F is {result} degrees C'


def convert_fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


if __name__ == '__main__':
    app.run()
