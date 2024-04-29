import os
import boto3

from flask import Blueprint, redirect, url_for, render_template, request, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from project.database import db, File, User

files_blueprint = Blueprint("files_bp", __name__)

session = boto3.Session(
                aws_access_key_id=os.getenv('ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('SECRET_ACCESS_KEY'),
                region_name=os.getenv('AWS_REGION')
                  )

s3 = session.resource('s3')
bucket = s3.Bucket(os.getenv('BUCKET_NAME'))


@files_blueprint.route('/files/<string:username>/')
def files(username):
    user = User.query.filter_by(username=username).first()
    if user:
        page = request.args.get('page', 1, type=int)
        per_page = 8

        if current_user.is_authenticated and current_user.username == username:
            files = File.query.filter_by(owner_id=user.id).order_by(File.created_at.desc()).paginate(page=page, per_page=per_page, error_out=False)
        else:
            files = File.query.filter_by(owner_id=user.id, public=True).order_by(File.created_at.desc()).paginate(page=page, per_page=per_page, error_out=False)
    else:
        return 404
    return render_template('files/files.html', username=username, user=user, files=files)


@files_blueprint.route('/info/<int:id>')
def info(id):
    return 

@login_required
@files_blueprint.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":

        if current_user.is_authenticated:
            form_file = request.files['file']
            public_check = request.form.get('public', False)
            public_check = True if public_check == 'on' else False
            
            if form_file:
                if form_file.content_length > 20 * 1024 * 1024:
                    pass
                else:
                    # Uploading a file  
                    filename = secure_filename(form_file.filename)
                    bucket.upload_fileobj(form_file, filename)
                    # Checking if file was uploaded
                    check_file = bucket.Object(filename)
                    try:
                        # Get the object
                        response = check_file.get()
                        if response['Body'].read():
                            object_url = f"https://{os.getenv('BUCKET_NAME')}.s3.{os.getenv('AWS_REGION')}.amazonaws.com/{filename}"
                            new_db_file_obj = File(owner_id=current_user.id, filename=filename, file_url=object_url, public=public_check)
                            db.session.add(new_db_file_obj)
                            db.session.commit()
                    
                    except s3.meta.client.exceptions.NoSuchKey:
                        return redirect(url_for('main_bp.dashboard'))
                
        else:
            flash("You must be logged in!")
            return redirect(url_for('auth_bp.login'))

        
    return redirect(url_for('main_bp.dashboard'))