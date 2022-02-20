from flask import Flask # first import
from flask_sqlalchemy import SQLAlchemy # second import : database
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sldkfslkfja92834@$Gas9824'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)








from application import routes
