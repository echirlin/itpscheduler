from flask import Blueprint, render_template, request, url_for, jsonify
from itpscheduler import app

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/members', methods=['GET', 'POST'])
def members():
    return jsonify({0: "wow"})

@bp.route('/members/<member_id>', methods=['GET', 'PUT'])
def member():
    return
