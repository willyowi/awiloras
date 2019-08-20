# from flask import render_template,redirect,url_for,abort,flash,request
# from .. import db
# from . import main
# from flask_login import login_required,current_user
# from ..models import User
# from .forms import Session_typesForm,SessionForm
# from ..image_upload import add_profile_pic,add_drift_image
from flask import render_template,request,redirect,url_for,abort,flash,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Session
from ..import db

#views
@main.route('/')
def index():

  '''
  View root page function that returns the index page and its data
  '''
  
  return render_template('index.html',user=current_user)
