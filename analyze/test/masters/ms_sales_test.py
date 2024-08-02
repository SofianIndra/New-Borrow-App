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
    getData = client.get('/ms-sales/')
    status_code = getData.status_code
    assert status_code == 200


# Test Get Selected Data by Cust Code
def test_get_selected_data_by_cust_code(client):
    # Read Selected Data
    custCode = 'AASY001'
    getData = client.get(f'/ms-sales/{custCode}')
    status_code = getData.status_code
    assert status_code == 200


# Test Failed Get Selected Data
def test_failed_get_selected_data(client):
    # Read Selected Data
    code ='12312313'
    getData = client.get(f'/ms-sales/{code}')
    status_code = getData.status_code
    assert status_code == 404
    

# Test Get Selected Data by Sales Code
def test_get_selected_data_by_sales_code(client):
    # Read Selected Data
    salesCode = 'AKS'
    getData = client.get(f'/ms-sales/sales/{salesCode}')
    status_code = getData.status_code
    assert status_code == 200