URL = "sqlite:///:memory:"


class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username


class Engine:
    def __init__(self, url):
        self.url = url


class Connection:
    def __init__(self, engine: Engine):
        self.engine = engine

    def get_user(self, username: str):
        return User(username)

    def close(self):
        print("closed connection")


def get_engine(url=URL):
    return Engine(url)


def get_connection(engine=None):
    if engine is None:
        engine = get_engine()
    return Connection(engine)


def get_user(username):
    conn = get_connection()
    return conn.get_user(username)
