from .import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id): 
    return User.query.get(int(user_id))

class SessionType(db.Model):
    __tablename__='session_types'
    
    id=db.Column(db.Integer,primary_key=True)
    session=db.Column(db.String(20))
    sessions=db.relationship('Session',backref='session',lazy='dynamic')



class User(db.Model,UserMixin):
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(50),unique=True,index=True)
    phone_number=db.Column(db.Integer)
    password_hash=db.Column(db.String(128))
    #creating a relationship between a user an sessions table
    sessions=db.relationship('Session',backref='user',lazy='dynamic')

    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def save_user(self):
        '''
        save instance for a user
        '''
        db.session.add(self)
        db.session.commit()  

    def __repr__(self):
        return f'User {self.username}'

class Session(db.Model):
    __tablename__='sessions'

    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))

    task=db.Column(db.String)
    time=db.Column(db.Integer)
    session_id=db.Column(db.Integer,db.ForeignKey('session_types.id'))

    def save_session(self):
        '''
        Function that saves a drift post
        '''
        db.session.add(self)
        db.session.commit()