from flask_migrate import Migrate
from flask import flask
from .models import db
from .app import create_app


app = create_app()

migrate = Migrate(app, db)


