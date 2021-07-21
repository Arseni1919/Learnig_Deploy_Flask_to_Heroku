import time

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Blueprint, render_template, redirect, url_for
from functions import *

analysis_bp = Blueprint('analysis_bp', __name__,
                        template_folder='templates',
                        static_folder='static',)  #static_url_path='/analysis')

scheduler = BackgroundScheduler()
scheduler.start()

list_to_print = []


# @scheduler.scheduled_job('interval', seconds=1, id='time_list')
def timed_job():
    if len(list_to_print) > 4:
        print(f'len of the list: {len(list_to_print)}')

        scheduler.remove_job('time_list')
    else:
        list_to_print.append(datetime.datetime.now())



job = scheduler.add_job(timed_job, 'interval', seconds=1, id='time_list')


@analysis_bp.route('/')
def analysis_home_func():
    # status: active, "", disabled
    nav_bar_titles = get_navbar_titles('Home', 'active')
    return render_template('analysis/analysis.html', nav_bar_titles=nav_bar_titles, list_to_print=list_to_print)


@analysis_bp.route('/refresh')
def refresh_func():
    # status: active, "", disabled
    names_of_jobs = [item.id for item in scheduler.get_jobs()]
    scheduler.print_jobs()

    if 'time_list' not in names_of_jobs:
        print(f'names_of_jobs: {names_of_jobs} and entered inside the if statement')
        scheduler.add_job(timed_job, 'interval', seconds=1, id='time_list')

    return redirect(url_for('analysis_bp.analysis_home_func'))


@analysis_bp.route('/clear')
def clear_func():
    # status: active, "", disabled
    list_to_print.clear()
    return redirect(url_for('analysis_bp.analysis_home_func'))




