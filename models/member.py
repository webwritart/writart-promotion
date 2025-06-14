from sqlalchemy.orm import backref

from extensions import db
from flask_login import UserMixin


member_role = db.Table('member_role',
                       db.Column('member_id', db.Integer, db.ForeignKey('member.id')),
                       db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
                       )

member_vid_edit_project = db.Table('member_vid_edit_project',
                       db.Column('member_id', db.Integer, db.ForeignKey('member.id')),
                       db.Column('vid_edit_project_id', db.Integer, db.ForeignKey('vid_edit_project.id'))
                       )

class Member(UserMixin, db.Model):
    __tablename__ = "member"

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    phone = db.Column(db.String(15), unique=True)
    whatsapp = db.Column(db.String(15))
    profession = db.Column(db.String(100))
    sex = db.Column(db.String(10))
    dob = db.Column(db.String(15))
    state = db.Column(db.String(100))
    website = db.Column(db.String(100))
    registration_date = db.Column(db.String(50))
    token = db.Column(db.String(10))
    role = db.relationship('Role', secondary=member_role, backref='members')
    vid_edit_project = db.relationship('VidEditProject', secondary=member_vid_edit_project, backref='members')

    def __repr__(self):
        return f'{self.name.split()[0]} -- {self.email}'


class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(500))

    def __repr__(self):
        return f'{self.name}'


class VidEditProject(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    models = db.Column(db.String(20))
    animation = db.Column(db.String(20))
    cut = db.Column(db.String(20))
    edit = db.Column(db.String(20))
    vfx = db.Column(db.String(20))
    color = db.Column(db.String(20))
    audio = db.Column(db.String(20))


    def __repr__(self):
        return f'{self.name}'



