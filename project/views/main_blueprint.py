from flask import Blueprint, redirect, url_for, render_template, request

from flask_login import login_required, current_user

from project.database import File

main_blueprint = Blueprint("main_bp", __name__)


@main_blueprint.route('/')
def index():
    if current_user.is_authenticated:
        page = request.args.get('page', 1, type=int)
        per_page = 8
        files = File.query.filter_by(public=True).order_by(File.created_at.desc()).paginate(page=page, per_page=per_page, error_out=False)
        return render_template('home/home_logged.html', files=files)
    else:
        return render_template('home/home_unlogged.html')


@login_required
@main_blueprint.route('/dashboard')
def dashboard():
    if current_user.is_authenticated:
        user = current_user
        private_files = File.query.filter_by(owner_id=current_user.id, public=False).all()
        public_files = File.query.filter_by(owner_id=current_user.id, public=True).all()
    else:
        return redirect(url_for('auth_bp.login'))
    return render_template('home/dashboard.html', user=user, private_files=private_files, public_files=public_files)