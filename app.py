from flask import Flask
from pages.home.home import home_bp

app = Flask(__name__)

app.register_blueprint(home_bp)


# @app.route('/')
# def hello_world():
#     return 'This is a version 3! mazafakaaaa yuhuuuu'


if __name__ == '__main__':
    app.run()
