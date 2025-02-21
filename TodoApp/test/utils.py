from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from ..database import Base
from ..main import app
from fastapi.testclient import TestClient
from ..models import Todos, Users
from ..routers.auth import bcrypt_context
import pytest

DATABASE_URL = 'mysql+pymysql://root:Jojo%40123@127.0.0.1:3306/test_db'

engine = create_engine(DATABASE_URL, poolclass=StaticPool)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    return {'username': 'john_doe', 'id': 1, 'user_role': 'admin'}


client = TestClient(app)


@pytest.fixture
def test_todo():
    db = TestingSessionLocal()

    db.execute(
        text(
            "INSERT INTO users (id, username, hashed_password, role, is_active) "
            "VALUES (1, 'john_doe', 'hashedpassword', 'admin', 1) "
            "ON DUPLICATE KEY UPDATE username=username;"
        )
    )
    db.commit()

    todo = Todos(
        id = 1,
        title="Learn to Code!",
        description="Learn to code everyday.",
        priority=5,
        complete=False,
        owner_id=1,
    )

    db.add(todo)
    db.commit()
    
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.execute(text("DELETE FROM users WHERE id = 1;"))
        connection.commit()

@pytest.fixture
def test_user():
    
    # To set teh default id 1 for test case purpose
    # db.execute(text("ALTER TABLE todos AUTO_INCREMENT = 1;"))
    # db.commit()
    
    user = Users(
        username = "john_doe",
        email = "john.doe@example.com",
        first_name = "John",
        last_name = "Doe",
        hashed_password = bcrypt_context.hash("SecurePass123!"),
        role = "admin",
        phone_number = "(111)-111-1111"
    )
    
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    
    yield user
    
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()