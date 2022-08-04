from datetime import datetime
from app import db


class Login1(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64))

    def __repr__(self):
        return '<Login1 {}>'.format(self.username)

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(64), index=True, unique=True) 
    rests=db.relationship('Rest', backref='area_name', lazy='dynamic')

class Rest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    res_name = db.Column(db.String(140))
    res_Address = db.Column(db.String(140))
    res_Cusine = db.Column(db.String(140))
    res_Rating = db.Column(db.String(140))
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'))

    def __repr__(self):
        return '<Rest {}>'.format(self.res_name)








