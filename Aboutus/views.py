from flask import Blueprint, render_template

Aboutus_blueprint = Blueprint('Aboutus', __name__, template_folder='templates')


@Aboutus_blueprint.route('/Aboutus')
def Aboutus():
    return render_template('Aboutus/Aboutus.html')


