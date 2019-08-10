#!/usr/bin/env python

from flask import Flask

from app.api.message import create_message_api

class Server:
  def __init__(self):
    self._app = Flask(__name__)

    # @app.route('/')
    @self._app.route('/')
    def hello_world():
      return 'Hello World'

    message_api = create_message_api(url_prefix='/api')
    self._app.register_blueprint(message_api)

  def run(self, host='0.0.0.0', port=5000):
    self._app.run(host=host,port=port)