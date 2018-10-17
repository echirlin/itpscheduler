from flask import Blueprint, render_template, request, url_for, jsonify
from itpscheduler import app
from itpscheduler.models import Member, Event, Assignment

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/members', methods=['GET', 'POST'])
def members():
    members = Member.query.order_by(Member.is_instructor.desc()).all()
    return jsonify({})

@bp.route('/members/<member_id>', methods=['GET', 'PUT'])
def member(member_id):
    member = Member.query.filter_by(id=member_id).first()
    return jsonify({})
