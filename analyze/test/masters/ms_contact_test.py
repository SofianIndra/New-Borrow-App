from api.main import app
from fastapi.testclient import TestClient
from pytest import fixture


@fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


# Test Get All Data
def test_get_all_data(client):
    # Read All Data
    getData = client.get('/ms-contact/')
    status_code = getData.status_code
    assert status_code == 200


# Test Get Selected Data
def test_get_selected_data(client):
    # Read Selected Data
    id = '1'
    getData = client.get(f'/ms-contact/{id}')
    status_code = getData.status_code
    assert status_code == 200
    
    
# Test Failed Get Selected Data
def test_failed_get_selected_data(client):
    # Read Selected Data
    id =12312313
    getData = client.get(f'/ms-contact/{id}')
    status_code = getData.status_code
    assert status_code == 404

    
    
# Test Get Selected Data By Address Id
def test_get_selected_data_by_addressid(client):
    # Read Selected Data
    id = 10
    getData = client.get(f'/ms-contact/contact/{id}')
    status_code = getData.status_code
    assert status_code == 200
    
    
# Test Failed Get Data By Address Id
def test_failed_get_data_by_addressid(client):
    # Read Selected Data
    addressId = 382472389478927498
    getData = client.get(f'/ms-contact/contact/{addressId}')
    status_code = getData.status_code
    assert status_code == 404

