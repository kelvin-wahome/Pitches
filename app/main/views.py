from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required
from ..models import User, Pitch, Category


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    form = UpdateProfile()
    if user is None:
        abort(404)

    if form.validate_on_submit():
        User.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

    return render_template('profile/update.html', user=user.username, form=form)
