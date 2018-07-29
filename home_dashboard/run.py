#!/usr/bin/env python3

import sys
from home_dashboard import app, io

if __name__ == '__main__':
	reload(sys)
	sys.setdefaultencoding('utf-8')
	io.run(app)
