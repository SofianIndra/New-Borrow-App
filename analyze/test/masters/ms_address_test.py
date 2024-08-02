from api.main import app
from fastapi.testclient import TestClient
from pytest import fixture


@fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


# Test Get All Data
def test_get_all_data(client):
    getData = client.get('/ms-address/')
    status_code = getData.status_code
    assert status_code == 200


# Test Get Selected Data
def test_get_selected_data(client):
    id = 'ABOC002'
    getData = client.get(f'/ms-address/{id}')
    status_code = getData.status_code
    assert status_code == 200
    

# Test Failed Get Selected Data
def test_failed_get_selected_data(client):
    id = '13123'
    getData = client.get(f'/ms-address/{id}')
    status_code = getData.status_code
    assert status_code == 404
    
    
# Test Get Data Filter By CustCode
def test_get_selected_data_by_custcode(client):
    custCode = 'ABOC002'
    getData = client.get(f'/ms-address/address/{custCode}')
    status_code = getData.status_code
    assert status_code == 200


# Test Failed Get Data By CustCode
def test_failed_get_data_by_custcode(client):
    # Read Selected Data
    custCode = '3123123123'
    getData = client.get(f'/ms-address/address/{custCode}')
    status_code = getData.status_code
    assert status_code == 404

