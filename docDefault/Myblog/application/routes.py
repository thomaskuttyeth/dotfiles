from datetime import datetime

from flask import render_template
from application import app
from application.form import RegistrationForm


posts = [
    {'author':'Thomaskutty Reji',
    "datetime":datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    "content":'''So when I talk about coming at a niche from a different angle,
    this example is exactly what I mean''',
    'title':'Skint Dad',
    'image':None},
    {'author':'Michelle Thomas',
    "datetime":datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    "content":'''So having some content around how they can make a few extra''',
    'title':'Above Water',
    'image':None}
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts = posts)


@app.route('/register',methods = ['GET','POST'])
def register():
    form =RegistrationForm()
    if form.validate_on_submit():
        pass
    return render_template('registration.html', form = form,title = 'registration')

