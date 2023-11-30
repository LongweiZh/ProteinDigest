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
from controller import Root

if __name__ == "__main__":
	try:
		turbogears.start_server(Root())
	except ConfigurationError as exc:
		sys.stderr.write(str(exc))
		sys.exit(1)
