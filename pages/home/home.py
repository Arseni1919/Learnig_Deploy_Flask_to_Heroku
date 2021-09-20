from flask import Blueprint, render_template, request
from functions import *


home_bp = Blueprint('home_bp', __name__,
                    template_folder='templates',
                    static_folder='static',)  # static_url_path='assets')


@home_bp.route('/')
def home_func():
    # status: active, "", disabled
    nav_bar_titles = get_navbar_titles('Home', 'active')

    return render_template('home/home.html', nav_bar_titles=nav_bar_titles)


@home_bp.route('/about')
def about_func():
    # status: active, "", disabled
    nav_bar_titles = get_navbar_titles('About', 'active')
    return render_template('home/about.html', nav_bar_titles=nav_bar_titles)




# @home_bp.route('/view/<int:product_id>')
# def view(product_id):
#     product = Product.query.get(product_id)
#     return render_template('products/view.html', product=product)