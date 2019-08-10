from flask import Blueprint

def create_message_api(url_prefix=''):
  message_api = Blueprint('message',__name__, url_prefix=f'{url_prefix}/message')

  @message_api.route('/hello')
  def hello():
      return "hello"

  @message_api.route('/goodbye')
  def goodbye():
      return "goodbye"

  return message_api