from datetime import datetime
from app import db, app
import bcrypt
from flask_uploads import IMAGES, UploadSet, configure_uploads


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    # User authentication information.
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    # User information
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    # logging the date and time of all user registration
    registered_on = db.Column(db.DateTime, nullable=False)
    # logging the date and time of a user’s current login.
    current_login = db.Column(db.DateTime, nullable=True)
    # logging the date and time of a user’s previous login
    last_login = db.Column(db.DateTime, nullable=True)
    # creates a one-to-many relationship with Post

    def __init__(self, email, firstname, lastname, phone, password, role):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        # hashing a password and using salt for more protection
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.registered_on = datetime.now()
        self.current_login = None
        self.last_login = None


class Post(db.Model):
    __tablename__ = 'posts'

    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    recipe = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, title, recipe, ingredients, image, price):
        self.title = title
        self.recipe = recipe
        self.ingredients = ingredients
        self.image = image
        self.price = price


def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
