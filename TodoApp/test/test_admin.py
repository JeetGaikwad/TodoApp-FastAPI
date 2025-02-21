from ..main import app
from fastapi import status
from .utils import *
from ..routers.admin import get_current_user, get_db
from ..models import Todos

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

# def test_admin_read_all_authenticated(test_todo):
#     response = client.get("/admin/todo")
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == [{
#         'id': 1,
#         'complete': False,
#         'title': "Learn to Code!",
#         'description': "Learn to code everyday.",
#         'priority': 5,
#         'owner_id': 1
#     }]
    
    
# def test_admin_delete_todo(test_todo):
#     # db = TestingSessionLocal()
#     # todos = db.execute(text("SELECT * FROM todos;")).fetchall()
#     # print(f"DEBUG: Todos in DB: {todos}")  # 🔍 Check if todo exists
#     # db.close()
#     response = client.delete("/todo/todo/2")
#     assert response.status_code == status.HTTP_204_NO_CONTENT

# def test_admin_delete_todo_not_found():
#     response = client.delete("/todo/todo/99")
#     assert response.status_code == status.HTTP_404_NOT_FOUND
#     assert response.json() == {
#         'detail': 'Todo not found'
#     }