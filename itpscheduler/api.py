from flask import Blueprint, render_template, request, url_for, jsonify
from itpscheduler import app
from itpscheduler.models import Member, Event, Assignment

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/members', methods=['GET', 'POST'])
def members():
    members = Member.query.order_by(Member.is_instructor.desc()).all()
    return jsonify([m.serialize(True) for m in members])

@bp.route('/members/<member_id>', methods=['GET', 'PUT', 'DELETE'])
def member(member_id):
    member = Member.query.filter_by(id=member_id).first()
    return jsonify(member.serialize(True))

@bp.route('/events', methods=['GET', 'POST'])
def events():
    events = Event.query.order_by(Event.date.asc()).all()
    return jsonify([e.serialize(True) for e in events])

@bp.route('/events/<event_id>', methods=['GET', 'PUT', 'DELETE'])
def event(event_id):
    event = Event.query.filter_by(id=event_id).first()
    return jsonify(event.serialize(True))
