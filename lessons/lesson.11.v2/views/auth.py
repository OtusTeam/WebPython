from logging import getLogger
from werkzeug.exceptions import BadRequest
from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

from models import Session, User

logger = getLogger(__name__)

auth_app = Blueprint("auth_app", __name__)


@auth_app.route("/", endpoint="index")
def index():
    return render_template("auth/index.html")


def validate_username_and_password(username, password):
    if not (
        username
        and len(username) >= 3
        and password
        and len(password) >= 8
    ):
        raise BadRequest("Username has to be at least 3 symbols and password at least 8")


def get_username_and_password():
    username = request.form.get("username")
    password = request.form.get("password")
    validate_username_and_password(username, password)

    return username, password


def validate_username_unique(username: str):
    if Session.query(User).filter_by(username=username).count():
        raise BadRequest("Username already exists!")


@auth_app.route("/register/", methods=("GET", "POST"), endpoint="register")
def register():
    if current_user.is_authenticated:
        return redirect(url_for("auth_app.index"))

    if request.method == "GET":
        return render_template("auth/register.html")

    username, password = get_username_and_password()
    validate_username_unique(username)

    user = User(username, password)
    Session.add(user)

    try:
        Session.commit()
    except Exception:
        logger.exception("Failed to add user!")
        Session.rollback()

    login_user(user)
    return redirect(url_for("auth_app.index"))


@auth_app.route("/login/", methods=("GET", "POST"), endpoint="login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("auth_app.index"))

    if request.method == "GET":
        return render_template("auth/login.html")

    username, password = get_username_and_password()

    user = Session.query(User).filter_by(username=username).one_or_none()
    if not (user and user.password == User.hash_password(password)):
        raise BadRequest("Username or password invalid!")

    login_user(user)
    return redirect(url_for("auth_app.index"))


@auth_app.route("/logout/", methods=("GET", "POST"), endpoint="logout")
def logout():
    logout_user()
    return redirect(url_for("auth_app.index"))


@auth_app.route("/secret/", endpoint="secret")
@login_required
def secret():
    return "Secret info"
