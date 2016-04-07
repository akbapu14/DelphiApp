from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    infringers = [  # fake array of posts
        {
            'company': 'Patent Troll',
            'body': 'Patent #32342'
        },
        {
            'company': 'Patent Troll # 2',
            'body': 'Patent #32342'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           infringers=infringers)

# index view function suppressed for brevity

@app.route('/search', methods=['GET', 'POST'])
def keywordSearch():
    form = LoginForm()
    infringers = [  # fake array of posts
        {
            'company': 'Patent Troll',
            'body': 'Patent #32342'
        },
        {
            'company': 'Patent Troll # 2',
            'body': 'Patent #32342'
        }
    ]
    if form.validate_on_submit():
        flash(form.openid.data)
        return render_template('index.html',
                               title='Sign In',
                               infringers=infringers)
    return render_template('login.html',
                           title='Sign In',
                           form=form)
