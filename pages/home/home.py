from flask import Blueprint, render_template

home_bp = Blueprint('home_bp', __name__,
                    template_folder='templates',
                    static_folder='static',)  # static_url_path='assets')


@home_bp.route('/')
def home_func():
    return render_template('home/home.html')

# @home_bp.route('/view/<int:product_id>')
# def view(product_id):
#     product = Product.query.get(product_id)
#     return render_template('products/view.html', product=product)