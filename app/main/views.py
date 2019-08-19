from flask import render_template,redirect,url_for,abort,flash,request
from .. import db
from . import main
from flask_login import login_required,current_user
from ..models import User
from .forms import Session_typesForm,SessionForm
from ..image_upload import add_profile_pic,add_drift_image
