#!/usr/bin/python3
# -*- coding=utf-8 -*-

# ===================================
# @Filename: start.py
# @Author: Longwei Zhang
# @Create Time: 11/30/23 07:18
# @Email:lz539@georgetown.edu
# @Description: 
# ===================================

import sys
#import cherrypy
from controller import Root
from tg import AppConfig
from wsgiref.simple_server import make_server
import webhelpers2

if __name__ == "__main__":
	try:
		config = AppConfig(minimal=True, root_controller=Root())
		config.renderers = ['kajiki']
		config['helpers'] = webhelpers2
		application = config.make_wsgi_app()
		httpd = make_server('', 8080, application)
		httpd.serve_forever()
	except Exception as e:
		print("ERROR")
		print(e)