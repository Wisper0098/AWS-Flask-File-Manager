import random
import datetime
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()

def generate_user_id():
    return random.randint(100000, 999999)

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, default=generate_user_id())
    username = db.Column(db.String(20), nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=False)
    files = db.relationship("File", backref="owner")

    def __init__(self, username, password):
        self.username = username
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf8')

    def check_password_hash(self, password_hash, password):
        return bcrypt.check_password_hash(password_hash, password)

class File(db.Model):
    __tablename__ = "files"

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    filename = db.Column(db.Text, nullable=False)
    file_url = db.Column(db.Text, nullable=False)
    public = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, owner_id, filename, file_url, public=False):
        self.owner_id = owner_id
        self.filename = filename
        self.file_url = file_url
        self.public = public

    
    def get_owner(self):
        return User.query.filter_by(id=self.owner_id).first()
