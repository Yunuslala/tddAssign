import pytest
from app import app

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_route(client):
    response=client.get('/')
    assert response.status_code==200
    assert response.data==b'hello, World!'

    
def test_get_weather_info(client):
    for city in weather_data.keys():
        response = client.get(f'/weather/{city}')
        assert response.status_code == 200
        data = response.get_json()
        assert 'temperature' in data
        assert 'weather' in data
        assert data['temperature'] == weather_data[city]['temperature']
        assert data['weather'] == weather_data[city]['weather']