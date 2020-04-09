from flask import Flask, render_template
from flask_login import LoginManager

from models import Session, User
from views import auth_app

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY="wertyuiudo3874g2o91413/f'34/f134f17g893f781foirfgdjhf",
)

app.register_blueprint(auth_app, url_prefix="/auth")

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Session.query(User).filter_by(id=user_id).one_or_none()


@app.route('/')
def index():
    return render_template("index.html")


@app.teardown_request
def remove_session(*args):
    Session.remove()


if __name__ == "__main__":
    app.run(debug=True)
