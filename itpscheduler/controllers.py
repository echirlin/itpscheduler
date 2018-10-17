from flask import render_template, url_for
from itpscheduler import app
from itpscheduler.models import Member, Event, Assignment

@app.route('/')
def home():
    colors = ['b20000', '403a30', '238c85', 'e200f2', 'a65353',
                '665c33', '40f2ff', 'cc66b8', 'ffc8bf', 'd9d26c']
    members = Member.query.order_by(Member.is_instructor.desc()).all()
    for i in range(len(members)):
        members[i].print_color = colors[i]
    return render_template('home.html', members=members)
