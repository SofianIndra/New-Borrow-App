from api.main import app
from fastapi.testclient import TestClient
from pytest import fixture


@fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


# Test Get All Data
def test_get_all_data(client):
    getData = client.get('/ms-accessories/')
    status_code = getData.status_code
    assert status_code == 200


# Test Get Selected Data
def test_get_selected_data(client):
    id = '1'
    getData = client.get(f'/ms-accessories/{id}')
    status_code = getData.status_code
    assert status_code == 200


# Test Failed Get Selected Data
def test_failed_get_selected_data(client):
    id = '13123'
    getData = client.get(f'/ms-accessories/{id}')
    status_code = getData.status_code
    assert status_code == 404