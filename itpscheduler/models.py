from datetime import datetime
from itpscheduler import app, db


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    is_instructor = db.Column(db.Boolean, default=False)
    events = db.relationship('Assignment', back_populates='member')

    def __repr__(self):
        instructor = " - instructor" if self.is_instructor else ""
        return f'<Member: {self.name}{instructor}>'


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(256), default='', nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    is_school_open = db.Column(db.Boolean, default=True, nullable=False)
    members = db.relationship('Assignment', back_populates='event')

    def __repr__(self):
        return f'<Event: {self.date}>'


class Assignment(db.Model):
    __tablename__ = 'assignments'
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    member = db.relationship('Member', back_populates='events')
    event = db.relationship('Event', back_populates='members')
    is_lead_instructor = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Assignment: {self.member.name} on {self.event.date}>'
