from flask import Flask
from pages.home.home import home_bp
from pages.analysis.analysis import analysis_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(analysis_bp, url_prefix='/analysis')


# @app.route('/')
# def hello_world():
#     return 'This is a version 3! mazafakaaaa yuhuuuu'


if __name__ == '__main__':
    app.run()
