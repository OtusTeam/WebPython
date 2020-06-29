from flask import Flask, render_template
from flask_login import LoginManager

from models import User
from models.db import Session

from views.auth import auth_app


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='alsdfbalkfaelfasjfnadlfj23fjn3424nf',
)

login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(auth_app, url_prefix="/auth")


@login_manager.user_loader
def load_user(user_id):
    return Session.query(User).filter_by(id=user_id).one_or_none()


@app.route("/")
def index():
    return render_template('index.html')


@app.teardown_request
def remove_session(*args):
    Session.remove()


if __name__ == '__main__':
    app.run()
