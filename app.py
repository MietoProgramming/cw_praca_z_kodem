from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name="Kamil"):
    return render_template('hello.html', name=name)
