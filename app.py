import os
from flask import Flask, request, render_template
from functions import get_navbar_titles
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from pages.home.home import home_bp
from pages.analysis.analysis import analysis_bp

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.StagingConfig")
app.config.from_object(env_config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Result

app.register_blueprint(home_bp)
app.register_blueprint(analysis_bp, url_prefix='/analysis')


@app.route('/secret_key')
def secret_key():
    secret_key = app.config.get("SECRET_KEY")
    return f"The configured secret key is {secret_key}."


@app.route('/insert_result', methods=['POST'])
def insert_result():
    res1 = Result(url=request.form['url'],
                  result_all=request.form['result_all'],
                  result_no_stop_words=request.form['result_no_stop_words'])
    db.session.add(res1)
    db.session.commit()

    results = Result.query.all()

    nav_bar_titles = get_navbar_titles('Home', 'active')
    return render_template('home/home.html', nav_bar_titles=nav_bar_titles, results=results)

if __name__ == '__main__':
    app.run()
