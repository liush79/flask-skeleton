from flask import Flask
from flask import render_template
from views import menu_0
from views import menu_1
from views import menu_2

app = Flask(__name__, static_url_path='', static_folder='static')
app.register_blueprint(menu_0.bp)
app.register_blueprint(menu_1.bp)
app.register_blueprint(menu_2.bp)


@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(500)
@app.errorhandler(503)
def page_not_found(e):
    return render_template('common/error.html', code=e.code, name=e.name, desc=e.description), e.code

