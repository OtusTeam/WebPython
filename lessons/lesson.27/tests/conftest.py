import pytest
import sqlalchemy


@pytest.fixture
def engine():
    return sqlalchemy.create_engine('sqlite://')

@pytest.fixture
def engine_with_table_users(engine):
    engine.execute('CREATE TABLE users (username VARCHAR);')
    yield engine
    engine.execute('DROP TABLE users;')
