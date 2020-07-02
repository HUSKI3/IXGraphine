from flask import render_template
from . import home
import os
import subprocess

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    #os.system('apt-cache search crypto')
    out = subprocess.Popen(['apt-cache', 'search', 'crypto'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    print(stdout)
    col=len(str(stdout).replace('\\n', '\n').split(str("\n")))
    print(col)
    crypto=str(stdout).replace('\\n', '\n').split(str("\n"))
    return render_template('page/home/index.html',crypto=crypto,col=col, title="Home Page")


@home.route('/dashboard')
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('page/home/dashboard.html', title="Dashboard")
