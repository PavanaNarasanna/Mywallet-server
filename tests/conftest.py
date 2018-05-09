import pytest
from server.database import db_session as session, engine
from server import app
from sqlalchemy import event
from server.database import SeedData


@pytest.fixture
def client():
    app.testing = True
    test_client = app.test_client()

    def teardown():
        pass

    return test_client


@pytest.fixture(scope="session")
def seeds():
    """Load the test fixture/seed data once for the whole test session"""
    seed_data = SeedData()
    return seed_data


@pytest.yield_fixture(scope='function')
def db_session():  # used to have the 'db' fixture as a param
    """
    Creates a new database session for a test. Note you must use this fixture
    if your test connects to db.

    Here we not only support commit calls but also rollback calls in tests,
    :coolguy:.
    """
    connection = engine.connect()
    # connection = db.engine.connect()
    transaction = connection.begin()

    # options = dict(bind=connection, binds={})
    # session = db.create_scoped_session(options=options)

    session.begin_nested()

    # session is actually a scoped_session
    # for the `after_transaction_end` event, we need a session instance to
    # listen for, hence the `session()` call
    @event.listens_for(session(), 'after_transaction_end')
    def restart_savepoint(sess, trans):
        if trans.nested and not trans._parent.nested:
            session.expire_all()
            session.begin_nested()

    # db.session = session

    yield session

    session.remove()
    transaction.rollback()
    connection.close()
