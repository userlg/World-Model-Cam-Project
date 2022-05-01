from flask import render_template, Blueprint, redirect, jsonify, request, make_response
from werkzeug.security import generate_password_hash
from ..models.users import User



auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route('/signup',methods=['GET','POST'])
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

@auth_bp.route('/login/<id>',methods=['POST'])
def login(id: str):
   try:
         #result = User.objects(id=id).first_or_404()
         result = User.objects.get_or_404(id=id)

         if result != None:
           return jsonify(result)
   except User.DoesNotExist as e:
        print(e)
        return jsonify({"message":" A problem happened","error":e}),501
    



@auth_bp.route('/logout',methods=['GET'])
def logout():
    pass

