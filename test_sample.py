import requests
import my_convecter


# Проверка соединения c api сайта
def test_get_locations_for_url():
    response = requests.get(my_convecter.url)
    assert response.status_code == 200

# Проверка что базовая валюта USD
def test_base_usd():
    response = requests.get(my_convecter.url)
    response_body = response.json()
    assert response_body['base']== 'USD'
