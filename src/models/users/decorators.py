from functools import wraps
from src.app import app
from flask import session, url_for, request
from werkzeug.utils import redirect


def requires_login(func):
    @wraps(func)
    def decoreted_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] is None:
            return redirect(url_for('users.login_user', next=request.path))
        return func(*args, **kwargs)
    return decoreted_function


def requires_admin_permissions(func):
    @wraps(func)
    def decoreted_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] is None:
            return redirect(url_for('users.login_user', next=request.path))
        if session['email'] not in app.config ['ADMINS']:
            return redirect(url_for('users.login_user'))
        return func(*args, **kwargs)
    return decoreted_function

