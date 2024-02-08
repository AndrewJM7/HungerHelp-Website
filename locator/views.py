from flask import Blueprint, render_template

locator_blueprint = Blueprint('locator', __name__, template_folder='templates')


@locator_blueprint.route('/locator')
def locator():
    return render_template('locator/locator.html')


