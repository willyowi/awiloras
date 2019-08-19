from flask import render_template,redirect,url_for,request,flash
from . import auth
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from flask_login import login_user,login_required,logout_user


@auth.route('/login',methods=['GET','POST'])
def login()
    form=LoginForm()


    