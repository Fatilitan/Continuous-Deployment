import pytest
from flask.testing import FlaskClient

from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_addition(client: FlaskClient):
    response = client.post('/calculate', data={'num1': '2', 'num2': '3', 'operation': 'add'})
    assert b'Result: 5.0' in response.data

def test_subtraction(client: FlaskClient):
    response = client.post('/calculate', data={'num1': '5', 'num2': '3', 'operation': 'subtract'})
    assert b'Result: 2.0' in response.data

def test_multiplication(client: FlaskClient):
    response = client.post('/calculate', data={'num1': '4', 'num2': '6', 'operation': 'multiply'})
    assert b'Result: 24.0' in response.data

def test_division(client: FlaskClient):
    response = client.post('/calculate', data={'num1': '8', 'num2': '2', 'operation': 'divide'})
    assert b'Result: 4.0' in response.data