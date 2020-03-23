URL = 'sqlite:///:memory:'


class User:
    def __init__(self, username: str):
        self.username = username


class Engine:
    def __init__(self, url):
        self.url = url


class Connection:
    def __init__(self, engine: Engine):
        self.engine = engine

    def request_admin(self):
        return User('admin')

    def close(self):
        print('closed')

    def request_user(self):
        return User('user')


def create_engine(url):
    return Engine(url)


def create_connection(engine):
    return Connection(engine)


def get_connection(url=URL):
    engine = create_engine(url)
    conn = create_connection(engine)
    return conn


def get_admin():
    conn = get_connection()
    return conn.request_admin()
