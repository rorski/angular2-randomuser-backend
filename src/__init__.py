import binascii
import os
from flask import Flask

from models import *
from src.settings import DB_URI

app = Flask(__name__)
app.secret_key = binascii.hexlify(os.urandom(24))
app.config['UPLOAD_FOLDER'] = os.getcwd() + '/static/media'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# https://github.com/jfinkels/flask-restless/issues/409
db.app = app
db.init_app(app)
#with app.app_context():
#    db.create_all()

import src.views
