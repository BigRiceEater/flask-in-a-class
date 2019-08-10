from flask import Blueprint

bp = Blueprint('message',__name__, url_prefix='/message')

@bp.route('/hello')
def hello():
    return "hello"

@bp.route('/goodbye')
def goodbye():
    return "goodbye"