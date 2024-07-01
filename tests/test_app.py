import pytest
from flask import Flask
from bs4 import BeautifulSoup
from app.routes import bp


@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(bp)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_redirect(client):
    response = client.get('/')
    assert response.status_code == 302
    assert response.headers['Location'] == '/report/'


def test_report_page(client):
    response = client.get('/report/')
    assert response.status_code == 200

    soup = BeautifulSoup(response.data, 'html.parser')
    assert soup.find('h1').text == 'Racing Report'
    assert soup.find('table') is not None


def test_drivers_page(client):
    response = client.get('/report/drivers/')
    assert response.status_code == 200
    soup = BeautifulSoup(response.data, 'html.parser')
    assert soup.find('h1').text == 'Drivers List'
    assert len(soup.find_all('li')) > 0


def test_driver_info_page(client):
    response = client.get('/report/drivers/?driver_id=SVF')
    assert response.status_code == 200
    soup = BeautifulSoup(response.data, 'html.parser')
    assert soup.find('h1').text == 'Driver Information'
    assert 'Sebastian Vettel' in soup.text


def test_driver_not_found(client):
    response = client.get('/report/drivers/?driver_id=XYZ')
    assert response.status_code == 404
    assert b'Driver ID not found' in response.data

