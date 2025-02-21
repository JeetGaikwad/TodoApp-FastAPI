from .utils import *
from ..routers.auth import authenticate_user, get_db, create_accesss_token, SECRET_KEY, ALGORITHM, get_current_user
from jose import jwt
from datetime import timedelta
from fastapi import HTTPException

app.dependency_overrides[get_db] = override_get_db

def test_authenticate_user(test_user):
    db = TestingSessionLocal()
    
    authenticated_user = authenticate_user(test_user.username, test_user.hashed_password, db)
    assert authenticated_user is not None
    # assert authenticated_user.username == test_user.username
    
    # it can also be created for username and password individually
    non_exist_user = authenticate_user('wronguser', 'pass', db)
    assert non_exist_user is False
    

def test_create_access_token():
    username = 'testuser'
    user_id = 1
    role = 'user'
    expires_delta = timedelta(days=1)
    
    token = create_accesss_token(username, user_id, role, expires_delta)
    
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM], options={'verify_signature': False})
    
    assert decoded_token['sub'] == username
    assert decoded_token['id'] == user_id
    assert decoded_token['role'] == role
  
@pytest.mark.asyncio  
async def test_get_current_user():
    encode = { 'sub': 'testuser',
                'id' : 1,
                'role' : 'admin'}
    
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
    
    user = await get_current_user(token=token)
    assert user == {'username': 'testuser', 'id': 1, 'user_role':'admin'}
    

@pytest.mark.asyncio
async def test_get_current_user_missing_payload():
    encode = {'role':'user'}
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
    
    with pytest.raises(HTTPException) as execinfo:
        await get_current_user(token=token)
        
    assert execinfo.value.status_code == 401
    assert execinfo.value.detail == 'Could not validate user.'
    