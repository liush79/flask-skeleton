from flask import abort
from flask import Blueprint
from flask import render_template

bp = Blueprint('menu_0', __name__, url_prefix='/menu_0')


@bp.route('/', methods=['GET'])
def view_dashboard():
    try:
        render_data = {

        }
        return render_template('template_menu_0/dashboard.html', render_data=render_data)
    except Exception, e:
        print 'Exception,', str(e)
        abort(500)
