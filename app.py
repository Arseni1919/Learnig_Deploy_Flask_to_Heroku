from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is a new version yuhuuuu'


if __name__ == '__main__':
    app.run()
