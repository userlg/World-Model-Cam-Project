from flask import render_template, Blueprint, redirect, jsonify, request
from werkzeug.security import generate_password_hash
from ..models.users import User


auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route('/signup',methods=['GET','Post'])
def signup():
    
    try:
        body = request.get_json()
        body['password'] = generate_password_hash(body['password'])
        user = User(**body).save()
        message = {"message":"Operation Successfull"}
        return jsonify(message,user),201
    except Exception as e:
        message = {"message":"Error Adding New User"}
        return jsonify(message),501
