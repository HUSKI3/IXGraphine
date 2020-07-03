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
    tag = 'crypto'
    out = subprocess.Popen(['apt-cache', 'search', 'crypto'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    print(stdout)
    col=len(str(stdout).replace('\\n', '\n').split(str("\n")))
    print(col)
    crypto=str(stdout).replace('\\n', '\n').split(str("\n"))
    return render_template('page/home/index.html',tag=tag,crypto=crypto,col=col, title="Home Page")

@home.route('appinstall/<tag>/<appid>')
def appinstall(tag,appid):
    """
    Render the app page for the appid which isnt an id but an index of the list because im dumb but yeah
    """
    print("Install appid:",appid)
    print("Grabbing application list...")
    out = subprocess.Popen(['apt-cache', 'search', str(tag)], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    col=len(str(stdout).replace('\\n', '\n').split(str("\n")))
    crypto=str(stdout).replace('\\n', '\n').split(str("\n"))
    """
    This is hella inffectient and may break if a new application with the tag was added, update this upon v0.30
    """
    print("Indexing...")
    index = crypto.index(str(appid))
    print("Got index: ",index)
    print("Building version data...")
    out = subprocess.Popen(['apt-cache','policy', str(appid.split(" ")[0])], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    data=str(stdout).replace('\\n', '\n').split(str("\n"))
    print(data)
    version = data
    cmd = str('apt show -a '+appid.split(" ")[0])
    out = subprocess.Popen(cmd.split(" "), 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    data=str(stdout).replace('\\n', '\n').split(str("\n"))
    print(data)
    data.pop(0)
    data = [s for s in data if "Description:" in s]
    return render_template('page/apps/app_page.html',data=data[0],version=version,appid=appid,index=index, title=str(appid))

@home.route('/dashboard')
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('page/home/dashboard.html', title="Dashboard")
