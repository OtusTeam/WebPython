URL = "sqlite:///:memory:"


class User:

    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username

    def save(self):
        print("saved", self)
        return self

    def delete(self):
        print("deleted", self)
        return True


class Engine:
    def __init__(self, url):
        self.url = url

    def check(self):
        print("check url", self.url)
        return self.url


class Connection:
    def __init__(self, engine):
        self.engine = engine

    def get_user(self, username):
        print(self.engine)
        return User(username)


def get_engine(url=URL):
    engine = Engine(url)
    engine.check()
    # engine.connect()
    return engine


def get_connection(engine=None):
    if engine is None:
        engine = get_engine()
    return Connection(engine)


def get_user(username):
    conn = get_connection()
    return conn.get_user(username=username)


def get_article():
    conn = get_connection()
    return conn.get_article()
