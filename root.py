#!/usr/bin/python3
# -*- coding=utf-8 -*-

# ===================================
# @Filename: root.py
# @Author: Longwei Zhang
# @Create Time: 11/30/23 06:51
# @Email:lz539@georgetown.edu
# @Description: 
# ===================================

# Define a controller
from tg import expose, TGController


class RootController(TGController):
	@expose()
	def index(self):
		return 'Hello World'

	@expose('hello.xhtml')
	def hello(self, person=None):
		return dict(person=person)


# Create an actual application
from tg import MinimalApplicationConfigurator

config = MinimalApplicationConfigurator()
config.update_blueprint({
	'root_controller': RootController(),
	'renderers': ['kajiki']
})

application = config.make_wsgi_app()

# Serve the application
from wsgiref.simple_server import make_server

print("Serving on port 8080...")
httpd = make_server("", 8080, application)
httpd.serve_forever()
