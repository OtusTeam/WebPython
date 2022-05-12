from pytest import fixture

from app import app


@fixture
def client():
    app.config.update(
        SERVER_NAME="testapp.qwerty",
        WTF_CSRF_ENABLED=False,
    )
    with app.test_client() as client:
        with app.app_context():
            yield client
