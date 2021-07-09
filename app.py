from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is a version 3! mazafakaaaa yuhuuuu'


if __name__ == '__main__':
    app.run()
