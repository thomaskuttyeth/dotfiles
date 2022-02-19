
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators 
from wtforms.validators import DataRequired

# setting the flask application 
app = Flask(__name__) 
app.config['SECRET_KEY']='asdffakjsdofjalsdflajsd'


# root page 
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html') 


import psycopg2 as pg2
import psycopg2.extras 
connection = pg2.connect(
    dbname = 'dvdrental', 
    user = 'postgres', 
    password = 'supinf123', 
    host = 'localhost' 
)

# starting the cursor 
cursor = connection.cursor() 
cursor.execute('''
    SELECT first_name, last_name FROM actor
    lIMIT 200; 
'''
)
data = [] 
for i in cursor.fetchall():
    data.append(i)
newdata = [list(i) for i in data]
for i in range(len(newdata)):
    newdata[i].insert(0,i+1)
newdata = [tuple(i) for i in newdata] 
cursor.close()

@app.route('/customers')
def show_customers():
    return render_template('index.html',newdata = newdata) 



if __name__ =='__main__':
    app.run(debug = True)
