from flask import render_template, url_for
from itpscheduler import app
from itpscheduler.models import Member, Event, Assignment


def apply_colors(members):
    colors = ['e6194b', '3cb44b', 'ffe119', '4363d8', 'f58231',
            '911eb4', '46f0f0', 'f032e6', 'bcf60c', 'fabebe',
            '008080', 'e6beff', '9a6324', 'fffac8', '800000',
            'aaffc3', '808000', 'ffd8b1', '000075', '808080']
    for i in range(len(members)):
        members[i].print_color = colors[i]
    return members


@app.route('/', methods=['GET', 'POST'])
def home():
    members = Member.query.order_by(Member.is_instructor.desc()).all()
    members = apply_colors(members)
    return render_template('home.html', members=members)
