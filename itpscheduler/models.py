from datetime import datetime
from itpscheduler import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)


member_events = db.Table('member_events',
    db.Column('member_id', db.Integer, db.ForeignKey('member.id'), primary_key=True)
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True)
)


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    is_instructor = db.Column(db.Boolean, nullable=False)
    scheduled_events = db.relationship("Scheduled Event",
        backref='scheduled_member', lazy=True)

    def __repr__(self):
        out = f"Member('{self.name}')"
        if self.is_instructor:
            out = out + " - instructor"
        return out


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)