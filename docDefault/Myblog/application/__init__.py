from flask import Flask # first import
from flask_sqlalchemy import SQLAlchemy # second import : database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sldkfslkfja92834@$Gas9824'
from application import routes
