from flask import render_template,request,redirect,url_for,abort,flash,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Session
from ..import db


# Views
@main.route('/')
def index():

  '''
  View root page function that returns the index page and its data
  '''
  
  return render_template('index.html',user=current_user)
