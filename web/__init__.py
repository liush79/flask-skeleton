from flask import Blueprint
from flask import Flask
from flask import render_template
from menu_1 import bp as menu_1_bp
from menu_2 import bp as menu_2_bp

app = Flask(__name__, static_url_path='', static_folder='static')
root_bp = Blueprint('root', __name__, template_folder='/')
app.register_blueprint(root_bp, url_prifix='/')
app.register_blueprint(menu_1_bp, url_prifix='/menu_1')
app.register_blueprint(menu_2_bp, url_prifix='/menu_2')


@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(500)
@app.errorhandler(503)
def page_not_found(e):
    return render_template('common/error.html', code=e.code, name=e.name, desc=e.description), e.code

