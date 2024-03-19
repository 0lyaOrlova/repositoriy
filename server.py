from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Привет, Flask!"

@app.route('/queue')
def queue():
    params = {'title': 'Home page'}
    return render_template('queue.html', **params)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)