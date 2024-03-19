import json

from flask import Flask, render_template, redirect

from logicform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "yandexlyceum_secret_key"


@app.route('/')
@app.route('/index')
def index():
    params = {'username': "Ученик Яндекс Лицея!",
              'title': 'Home page'}
    return render_template('index.html', **params)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=33)

@app.route('/news')
def news():
    with open('news.json', "rt", encoding='utf8') as f:
        news_list = json.loads(f.read())
    return render_template('news.html', news=news_list)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/news')
    return render_template('login.html', title="Autorison", form=form)
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')