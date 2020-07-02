from logging import getLogger

from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.exceptions import BadRequest, InternalServerError

from models import User
from models.db import Session

logger = getLogger(__name__)

auth_app = Blueprint("auth_app", __name__)


@auth_app.route("/", endpoint="index")
def index():
    return render_template("auth/index.html", user=current_user)


def validate_user_credentials(username: str, password: str):
    if not (
        username
        and len(username) >= 3
        and password
        and len(password) >= 5
    ):
        raise BadRequest("Username has to be at least 3 symbols and pass min 5")


def get_username_and_password_from_form(form: dict):
    username = form.get("username")
    password = form.get("password")
    validate_user_credentials(username, password)

    return username, password


def validate_username_unique(username):
    if Session.query(User).filter_by(username=username).count():
        raise BadRequest(f"User with username {username!r} already exists!")


@auth_app.route("/register/", methods=("GET", "POST"), endpoint="register")
def register():
    if current_user.is_authenticated:
        return redirect(url_for("auth_app.index"))

    if request.method == "GET":
        return render_template("auth/register.html")

    username, password = get_username_and_password_from_form(request.form)
    validate_username_unique(username)

    user = User(username, password)
    Session.add(user)

    try:
        Session.commit()
    except Exception as e:
        logger.exception("Error creating user!")
        raise InternalServerError(f"Could not create new user! Error: {e}")

    login_user(user)
    return redirect(url_for("auth_app.index"))


@auth_app.route("/login/", methods=("GET", "POST"), endpoint="login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("auth_app.index"))

    if request.method == "GET":
        return render_template("auth/login.html")

    username, password = get_username_and_password_from_form(request.form)

    user = Session.query(User).filter_by(username=username).one_or_none()

    if not user:
        return render_template("auth/login.html", error_text="User not found")

    if user.password != User.hash_password(password):
        return render_template("auth/login.html", error_text="Invalid username or password!")

    login_user(user)
    return redirect(url_for("auth_app.index"))


@auth_app.route("/logout/", endpoint="logout")
def logout():
    logout_user()
    return redirect(url_for("auth_app.login"))


@auth_app.route("/protected/", endpoint="protected")
@login_required
def protected():
    return "<h1>SECRET INFO</h1>"
