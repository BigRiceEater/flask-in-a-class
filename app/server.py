#!/usr/bin/env python

from flask import Flask

class Server:
  def __init__(self):
    self._app = Flask(__name__)

    # @app.route('/')
    @self._app.route('/')
    def hello_world():
      return 'Hello World'

  def run(self, host='0.0.0.0', port=5000):
    self._app.run(host=host,port=port)