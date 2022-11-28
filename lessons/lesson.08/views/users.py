from flask import Blueprint, request

users_app = Blueprint("users_app", __name__)


@users_app.get("/me/")
def get_me():
    return {
        "agent": request.headers.get("user-agent")
    }
