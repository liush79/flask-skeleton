from flask import abort
from flask import Blueprint
from flask import render_template

bp = Blueprint('menu_0', __name__, url_prefix='/menu_0')


@bp.route('/', methods=['GET'])
def view_dashboard():
    try:
        sample_data = {
        }
        return render_template('template_menu_0/menu_0_dashboard.html', render_data=sample_data)
    except Exception, e:
        print 'Exception,', str(e)
        abort(500)
