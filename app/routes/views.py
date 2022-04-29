from flask import render_template, Blueprint

views_bp = Blueprint("views_bp", __name__)


@views_bp.route('/',methods=['GET'])
def index():

    #number = randint(1,10)

    return render_template('index.html')