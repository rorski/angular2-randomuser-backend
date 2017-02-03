import datetime
import phonenumbers

from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import PhoneNumberType
from marshmallow import Schema, fields

db = SQLAlchemy()

# Random User Model
###############################################################################
class User(db.Model):
    ''' A model for storing data pulled from random user '''
    __tablename__ = 'random_user'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30)) 
    lastname = db.Column(db.String(30))
    password = db.Column(db.String(92))
    gender = db.Column(db.String(6))
    dob = db.Column(db.DateTime)
    phone = db.Column(PhoneNumberType())
    email = db.Column(db.String(120),unique=True,index=True)
    # registered_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    # location
    city = db.Column(db.String(50))
    state = db.Column(db.String(20))

    summary = db.Column(db.String(250)) # profile summary from lorem ipsum
    pic = db.Column(db.String(60))

    def __init__(self, firstname, lastname, password, gender, dob, phone, email, city, state, summary, pic):
        self.firstname = firstname
        self.lastname = lastname
        self.set_password(password)
        self.gender = gender
        self.dob = dob 
        self.phone = phone
        self.email = email
        self.city = city
        self.state = state
        self.summary = summary
        self.pic = pic

    def set_password(self, password):
        self.password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User {} {}>'.format(self.firstname, self.lastname)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    firstname = fields.Str()
    lastname = fields.Str()
    password = fields.Str()
    gender = fields.Str()
    dob = fields.DateTime()
    phone = fields.Str()
    email = fields.Email()
    city = fields.Str()
    state = fields.Str()
    summary = fields.Str()
    pic = fields.Str()
