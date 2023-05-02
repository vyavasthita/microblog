from app import app
from flask import render_template, flash, redirect, url_for
from .forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Dilip'}
    posts = [
        {
            'author': {'username': 'Samskriit'},
            'body': 'Beautiful day in Jaipur!'
        },
        {
            'author': {'username': 'Sabhyata'},
            'body': 'Rang De Basanti movie was so cool!'
        }
    ]
    return render_template('base.html', title='Home', user=user, posts=posts)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        flash(f"Login requested for user {form.username.data}, Remember Me is {form.remember_me.data}")
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)