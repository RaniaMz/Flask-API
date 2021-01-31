from flask import jsonify, send_from_directory, request
from sqlalchemy import desc

from app import app
from app.models import Candidate, Department


def is_admin(headers):
    return headers.get("X-ADMIN") == "1"


@app.route("/list", methods=["GET"])
def list():
    if not is_admin(request.headers):
        return "Error Unauthorized", 401

    candidates = Candidate.query.join(Department).order_by(desc(Candidate.register_date)).all()

    return jsonify([{'candidate_id': candidate.candidate_id,
                     'full_name': candidate.full_name,
                     'birth_date': candidate.birth_date,
                     'experience_years': candidate.experience_years,
                     'department': candidate.Department.name}
                    for candidate in candidates])


@app.route("/download/<file_id>", methods=["GET"])
def download(file_id):
    if not is_admin(request.headers):
        return "Error Unauthorized", 401
    if not app.config['IS_CLOUD']:
        candidates = Candidate.query.filter_by(candidate_id=file_id).first()
        return send_from_directory("../"+app.config['UPLOAD_PATH'], candidates.resume_name)
    else:
        # for future use of cloud storage e.g : S3
        pass
