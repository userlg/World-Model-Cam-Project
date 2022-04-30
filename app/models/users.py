from flask_mongoengine import mongoengine as me
from flask import jsonify
from werkzeug.security import check_password_hash,generate_password_hash
import datetime


class User(me.Document):
    username = me.StringField(required=True,trim=True,unique=True)
    password = me.StringField(required=True)
    create_at = me.DateTimeField(required=True,default=datetime.datetime.now())
