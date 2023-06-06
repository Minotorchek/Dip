import requests
import pytest

# pytest tests/*
# python -m pytest -v -s    - чтобы увидеть ответ с data



def test_equal():
    assert 1 == 1, 'Number is not equal'


def test_call_call_endpoint():
    response = requests.get('http://127.0.0.1:8000/swagger')
    assert response.status_code == 200


ENDPOINT = 'http://127.0.0.1:8000/auth/'

@pytest.fixture
def test_get_admin_JWT():
    payload = {
        'email': '',
        'password': ''
    }

    response = requests.post('http://127.0.0.1:8000/auth/jwt/create', json=payload)
    assert response.status_code == 200

    data = response.json()
    token_admin = data['access']
    return token_admin
