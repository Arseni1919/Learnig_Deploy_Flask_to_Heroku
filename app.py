import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from pages.home.home import home_bp
from pages.analysis.analysis import analysis_bp

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///nt_database'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Result

app.register_blueprint(home_bp)
app.register_blueprint(analysis_bp, url_prefix='/analysis')


@app.route('/secret_key')
def secret_key():
    secret_key = app.config.get("SECRET_KEY")
    return f"The configured secret key is {secret_key}."


if __name__ == '__main__':
    app.run()
