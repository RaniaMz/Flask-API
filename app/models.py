from sqlalchemy import event

from app import db


class Candidate(db.Model):
    __tablename__ = 'candidate'
    candidate_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column("Full Name", db.String(100))
    birth_date = db.Column("Day of Birth", db.DateTime)
    experience_years = db.Column("Years of Experience", db.Integer)
    department_id = db.Column('Department ID', db.Integer, db.ForeignKey('department.id'), nullable=False)
    resume_name = db.Column("Resume", db.String(100))
    register_date = db.Column("Registration Date", db.DateTime, default=db.func.current_timestamp())

    def __init__(self, full_name, birth_date, experience_years, department_id, resume_name):
        self.full_name = full_name
        self.birth_date = birth_date
        self.experience_years = experience_years
        self.department_id = department_id
        self.resume_name = resume_name


class Department(db.Model):
    __tablename__ = 'department'

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    Candidates = db.relationship(Candidate, backref='Department')

    def __init__(self, name):
        self.name = name


@event.listens_for(Department.__table__, "after_create")
def create_department(*args, **kwargs):
    db.session.add(Department("HR"))
    db.session.add(Department("IT"))
    db.session.add(Department("Finance"))
    db.session.commit()
