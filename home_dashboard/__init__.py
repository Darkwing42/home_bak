from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO, send, emit
import os, sys
import json
import requests

#from home_dashboard.models import User, Survey, Question, Choice
#from utils import POSTGRES_DB, POSTGRES_PW, POSTGRES_URL, POSTGRES_USER

basedir = os.path.abspath(os.path.dirname(sys.argv[0]))
#DB_URL = 'postgres+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
DB_URL= 'sqlite:////home/darkwing/dev/home/home_dashboard/app.db'
app = Flask(__name__,
            static_folder='../home_dashboard_frontend/static',
            template_folder='../home_dashboard_frontend')

app.config['SECRET_KEY'] = "test_secret_key"

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
io = SocketIO(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

@io.on('connect')
def connect():

    print('Client connected... ')
    emit('connect', 'Client Successfully connected')

@io.on('message')
def message(payload):
    print(payload)
    send(payload)

@io.on('home_data')
def home_data():
    print('############ GOT REQUEST ################# ')
    homes = [
        {"id":1, "section_name": 'Nützliche Links', "urls":['www.gmx.net','www.zalando.de']},
        {"id":2, "section_name": 'Finanzen', "urls": ['www.comdirect.de']}
    ]


    [print(home) for home in homes]

    print('Sending data')
    emit('home_data', homes, json=True)
    #[ emit('home_data',home) for home in homes ]
    print('Successfully send data')
@io.on('todo_data')
def todo_data():
    todo_list = [
{ "id": 1, "list_name": 'Test', "tasks": [
  {"task_name": 'Einbürgerung', "done": "false" },
  {"task_name": 'Überweisung', "done": "false" }
],
"list_done": "false"
},
{"id": 2, "list_name": 'Einkauf', "tasks": [
  {"task_name": 'Milch', "done": "true"},
  {"task_name": 'Brot', "done": "false"}
],
"list_done": "false"
}
]
    emit('todo_data', todo_list)

@io.on('weather_data')
def weather_data(city):
  api_key = '6b21dea1b860e078964f59ba1c075972'
  url = 'http://api.openweathermap.org/data/2.5/weather?q='+ city +',de&&appid=6b21dea1b860e078964f59ba1c075972'
  actual_data = requests.get(url)
  print(actual_data)

  emit('weather_data', actual_data.json() , json=True)
