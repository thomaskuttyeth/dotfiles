from datetime import datetime

from flask import render_template,url_for,flash,redirect
from application import app,db,bcrypt
from application.form import RegistrationForm

from application.models import User,Post


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



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))

    return render_template('registration.html', title='Register', form=form)
