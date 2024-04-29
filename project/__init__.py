import os
from flask import Flask
from flask_login import LoginManager
from project.database import db
from project.views.auth_blueprint import auth_blueprint
from project.views.main_blueprint import main_blueprint
from project.views.files_blueprint import files_blueprint

app = Flask(__name__)
app.config.from_object("project.config.Config")

current_dir = os.path.dirname(__file__)
templates_dir = os.path.join(current_dir, '..', 'templates')
app.template_folder = templates_dir

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth_bp.login"

# Initialize SQLAlchemy
db.init_app(app)

# Register blueprints
app.register_blueprint(auth_blueprint, url_prefix="")
app.register_blueprint(main_blueprint, url_prefix="")
app.register_blueprint(files_blueprint, url_prefix="")

from project.database import User

# Define user loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
