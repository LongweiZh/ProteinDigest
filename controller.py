#!/usr/bin/python3
# -*- coding=utf-8 -*-

# ===================================
# @Filename: controller.py
# @Author: Longwei Zhang
# @Create Time: 11/30/23 06:51
# @Email:lz539@georgetown.edu
# @Description: 
# ===================================

# Define a controller
from tg import expose, TGController


class Root(TGController):
	@expose()
	def index(self):
		return 'Hello World'

	@expose('hello.xhtml')
	def hello(self, person=None):
		return dict(person=person)