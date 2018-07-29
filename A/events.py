from functools import wraps
from datetime import datetime, timedelta
from flask import current_app

import jwt
from .models import db, Survey, Question, choice, User


@io.on('login')
def login(payload):

	user = User.authenticate(**payload)

	if not user:
		return send({'message': 'Invalide credentials', 'authenticated': false })
	token = jwt.encode({
			'sub': user.email,
			'iat': datetime.now(),
			'exp': datetime.now() + timedelta(minutes=30)},
			current_app.config['SECRET_KEY'])
	return send({ 'token': token.decode('UTF-8') })

@io.on('get_surveys')
def get_surveys():

	surveys = Survey.query.all()
	return send(jsonify([s.to_dict() for s in surveys]))
