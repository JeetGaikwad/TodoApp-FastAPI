from ..main import app
from ..routers.todos import get_db, get_current_user
from fastapi import status
from .utils import *

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

# def test_read_all_authenticated(test_todo):
#     response = client.get("/todos")
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == [{
#         'id': 1,
#         'complete': False,
#         'title': "Learn to Code!",
#         'description': "Learn to code everyday.",
#         'priority': 5,
#         'owner_id': 1
#     }]

# def test_read_one_authenticated(test_todo):

#     response = client.get("/todos/todo/2")
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == {
#         'id': 2,
#         'complete': False,
#         'title': "Learn to Code!",
#         'description': "Learn to code everyday.",
#         'priority': 5,
#         'owner_id': 1
#     }
    
# def test_read_one_not_found(test_todo):

#     response = client.get("/todos/todo/999")
#     assert response.status_code == 404
#     assert response.json() == {
#         'detail': 'Todo not found'
#     }
    

# def test_create_todo(test_todo):
    
#     request_data = {
#     "title": "Finish project report",
#     "description": "Complete the final draft and submit it before the deadline.",
#     "priority": 3,
#     "complete": False
#     }

#     response = client.post("/todos/todo", json=request_data)
#     assert response.status_code == status.HTTP_201_CREATED

    
# def test_update_todo(test_todo):
#     # db = TestingSessionLocal()
#     # todos = db.execute(text("SELECT * FROM todos;")).fetchall()
#     # print(f"DEBUG: Todos in DB: {todos}")  # 🔍 Check if todo exists
#     # db.close()
    
#     request_data = {
#     "title": "Finish project report final",
#     "description": "Complete the final draft and submit it now.",
#     "priority": 3,
#     "complete": True
#     }

#     response = client.put("/todos/todo/6", json=request_data)
#     assert response.status_code == status.HTTP_204_NO_CONTENT

# def test_update_todo_not_found(test_todo):
#     # db = TestingSessionLocal()
#     # todos = db.execute(text("SELECT * FROM todos;")).fetchall()
#     # print(f"DEBUG: Todos in DB: {todos}")  # 🔍 Check if todo exists
#     # db.close()
    
#     request_data = {
#     "title": "Finish project report final",
#     "description": "Complete the final draft and submit it now.",
#     "priority": 3,
#     "complete": True
#     }

#     response = client.put("/todos/todo/66", json=request_data)
#     assert response.status_code == status.HTTP_404_NOT_FOUND
#     assert response.json() == {
#         'detail': 'Todo not found'
#     }

# def test_delete_todo(test_todo):
#     # db = TestingSessionLocal()
#     # todos = db.execute(text("SELECT * FROM todos;")).fetchall()
#     # print(f"DEBUG: Todos in DB: {todos}")  # 🔍 Check if todo exists
#     # db.close()
#     response = client.delete("/todos/todo/8")
#     assert response.status_code == status.HTTP_204_NO_CONTENT

# def test_delete_todo_not_found():
#     response = client.delete("/todos/todo/99")
#     assert response.status_code == status.HTTP_404_NOT_FOUND
#     assert response.json() == {
#         'detail': 'Todo not found'
#     }