from ..main import app
from fastapi import status
from .utils import *
from ..routers.user import get_current_user, get_db
from ..models import Todos

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

# def test_return_user(test_user):
#     response = client.get("/user")
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json()['username'] == 'john_doe'
#     assert response.json()['email'] == 'john.doe@example.com'
#     assert response.json()['first_name'] == 'John'
#     assert response.json()['last_name'] == 'Doe'
#     assert response.json()['role'] == 'admin'
    

# Works only when with fix user id because every time i create a test case the id changes
# user_model = db.query(Users).filter(Users.id == 2).first()
# def test_change_password_success(test_user):
#     db = TestingSessionLocal()
#     todos = db.execute(text("SELECT * FROM users;")).fetchall()
#     print(f"DEBUG: Todos in DB: {todos}")  
#     db.close()
    
#     response = client.put("/user/password", json={"password": "SecurePass123!", "new_password": "SecurePass123"})
#     assert response.status_code == status.HTTP_204_NO_CONTENT

# def test_change_password_invalid(test_user):
#     response = client.put("/user/password", json={"password": "secr!", "new_password": "ssded"})
#     assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    
# def test_change_phone_number_success(test_user):
#     response = client.put("/user/phonenumber/951-784-5884")
#     assert response.status_code == status.HTTP_204_NO_CONTENT