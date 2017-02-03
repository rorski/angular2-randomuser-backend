from flask import request, send_file, jsonify, abort

from src import app
from src.models import *

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route("/")
def index():
    ''' Base index '''
    abort(403)

@app.route('/api/v1/user', methods=['GET'])
def users():
    users = User.query.all()
    result = users_schema.dump(users)
    return jsonify({'results': result.data})

@app.route('/api/v1/user/<int:pk>', methods=['GET'])
def user_detail(pk):
    user = User.query.get(pk)
    result = user_schema.dump(user)
    return jsonify({'results': result.data})
