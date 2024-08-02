from api.main import app
from fastapi.testclient import TestClient
from pytest import fixture


@fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


# Test Get All Data
def test_get_all_data(client):
    getData = client.get('/ms-customer/')
    status_code = getData.status_code
    assert status_code == 200


# Test Get Selected Data
def test_get_selected_data(client):
    code = '3DNI001'
    getData = client.get(f'/ms-customer/{code}')
    status_code = getData.status_code
    assert status_code == 200
    
    
# Test Failed Get Selected Data
def test_failed_get_selected_data(client):
    custName ='12312313'
    getData = client.get(f'/ms-customer/{custName}')
    status_code = getData.status_code
    assert status_code == 404
    
    
# Test Get Selected Data By cust name
def test_get_selected_data_by_custname(client):
    custName = 'ANTABOGA AMERTA INDONESIA, PT'
    getData = client.get(f'/ms-customer/customer/{custName}')
    status_code = getData.status_code
    assert status_code == 200
    
    
# Test Failed Get Data By cust name
def test_failed_get_data_by_custname(client):
    custName = 'POS RONDA'
    getData = client.get(f'/ms-customer/customer/{custName}')
    status_code = getData.status_code
    assert status_code == 404
    
    
# Test Get Selected Data By DC Level
def test_get_selected_data_by_dc(client):
    parentCode = 'IDMR180'
    getData = client.get(f'/ms-customer/dc/{parentCode}')
    status_code = getData.status_code
    assert status_code == 200
    
    
# Test Failed Get Data By DC Level
def test_failed_get_data_by_dc(client):
    parentCode = 'IDMR1123180'
    getData = client.get(f'/ms-customer/dc/{parentCode}')
    status_code = getData.status_code
    assert status_code == 404
    
    
# Test Get Selected Data By Store Level
def test_get_selected_data_by_store(client):
    parentCode = 'DC SEMARANG-SAT'
    getData = client.get(f'/ms-customer/store/{parentCode}')
    status_code = getData.status_code
    assert status_code == 200
    
    
# Test Failed Get Data By Store Level
def test_failed_get_data_by_store(client):
    parentCode = 'DC GROGOL-SAT'
    getData = client.get(f'/ms-customer/store/{parentCode}')
    status_code = getData.status_code
    assert status_code == 404



