from flask import Flask, render_template, url_for
import secrets
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


load_dotenv()

# CONFIGURATION
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://csc2033_team06:Arid5Dye?Day@cs-db.ncl.ac.uk:3306/csc2033_team06'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lf41H4iAAAAALCDw0esznqOX1-uxAKABhCYQ51_'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Lf41H4iAAAAALw_t1vVYYcr9fUvBkqR7yjZqCwN'
app.config['UPLOADED_PHOTOS_DEST'] = 'images'
app.config['UPLOADS_DEFAULT_DEST'] = 'images'


# Initialise database
db = SQLAlchemy(app)

# A secret key to sign and validate session cookies
app.config['SECRET_KEY'] = secrets.token_hex(16)


# Register blueprints with app

from main.views import main_blueprint
from locator.views import locator_blueprint
from users.views import users_blueprint
from Aboutus.views import Aboutus_blueprint
from blog.views import blog_blueprint

app.register_blueprint(blog_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(locator_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(Aboutus_blueprint)


@app.errorhandler(400)
def bad_request_error(error):
    return render_template('errors/400.html'), 400


# Handles error:the server is refusing action. This may be due to the user not having permission
@app.errorhandler(403)
def forbidden_error(error):
    return render_template('errors/403.html'), 403


# Handles error: the requested resource could not be found but may be available in the future
@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


# Handles error:An unexpected condition happened.
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html'), 500


# Handles error:server is not ready to handle the request
@app.errorhandler(503)
def service_unavailable_error(error):
    return render_template('errors/503.html'), 503


if __name__ == '__main__':
    app.run()

