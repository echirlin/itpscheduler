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

    def serialize(self, deep=False):
        json = {
            'id': self.id,
            'name': self.name,
            'is_instructor': self.is_instructor
        }

        if deep:
            json['events'] = [a.serialize(self) for a in self.events]

        return json


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(256), default='', nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    is_school_open = db.Column(db.Boolean, default=True, nullable=False)
    members = db.relationship('Assignment', back_populates='event')

    def __repr__(self):
        return f'<Event: {datetime.strftime(self.date, "%b %d, %Y")}>'

    def serialize(self, deep=False):
        json = {
            'id': self.id,
            'notes': self.notes,
            'date': self.date.timestamp(),
            'is_school_open': self.is_school_open
        }

        if deep:
            json['members'] = [m.serialize(self) for m in self.members]

        return json


class Assignment(db.Model):
    __tablename__ = 'assignments'
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    member = db.relationship('Member', back_populates='events')
    event = db.relationship('Event', back_populates='members')
    is_lead_instructor = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Assignment: {self.member.name} on {self.event.date}>'

    def serialize(self, cls):
        json = {
            'is_lead_instructor': self.is_lead_instructor
        }
        
        if type(cls).__name__ == 'Member':
            json['event'] = self.event.serialize()
        elif type(cls).__name__ == 'Event':
            json['member'] = self.member.serialize()
        
        return json
