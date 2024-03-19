import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    params = {'username': "Ученик Яндекс Лицея!",
              'title': 'Home page'}
    return render_template('index.html', **params)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=33)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')