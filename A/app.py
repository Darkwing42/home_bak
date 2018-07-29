from flask import Flask

def create_app(app_name='TestApp'):
	app = Flask(app_name)

	#TODO: Config einbinden

	#TODO: import events
	
	from .models import db
	from .events import io

	db.init_app(app)
	io.init_app(app)

	return app
	
