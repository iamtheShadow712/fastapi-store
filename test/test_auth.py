import app.constants as CONSTANTS

def test_register(client):
    user = {
        "username": "test user 1",
        "email": "test1@email.com",
        "password": "testuser1"
    }
    res = client.post(f"/{CONSTANTS.API_VERSION}/auth/register", json=user)
    assert res.status_code == 201
    assert res.json().get('message') == "Registration Successfull"