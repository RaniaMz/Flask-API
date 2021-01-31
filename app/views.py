import os

from flask import request
from werkzeug.utils import secure_filename

from app import app, db
from app.models import Candidate


def is_valid_file(file_ext):
    return any([file_ext.endswith(ext) for ext in app.config['UPLOAD_EXTENSIONS']])


def save_file(file, file_name):
    if not app.config['IS_CLOUD']:
        file.save(os.path.join(app.config['UPLOAD_PATH'], file_name))
    else:
        # for future use of cloud storage e.g : S3
        pass


@app.route("/register", methods=["POST"])
def registration():
    upload_file = request.files['file']
    file_name = secure_filename(upload_file.filename)
    if file_name == '':
        return "No File Provided", 204
    if not is_valid_file(file_name):
        return "Invalid File", 400
    save_file(upload_file, file_name)
    candidate = Candidate(request.form['full_name'], request.form['birth_date'],
                          request.form['experience_years'],
                          request.form['department_id'], file_name)
    db.session.add(candidate)
    db.session.commit()
    return "Saved"
