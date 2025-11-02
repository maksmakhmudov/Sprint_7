# conftest.py
import pytest
import requests
from data import Data
from urls import Urls
from helpers import create_random_login, create_random_password, create_random_firstname


@pytest.fixture
def cleanup_courier():
    """Фикстура для очистки созданного курьера после теста"""
    courier_ids = []
    courier_logins = []
    
    yield courier_ids, courier_logins
    
    for courier_id in courier_ids:
        requests.delete(f"{Urls.URL_courier_create}/{courier_id}")


@pytest.fixture
def create_test_courier():
    """Фикстура для создания тестового курьера и возврата его данных"""
    login = create_random_login()
    password = create_random_password()
    first_name = create_random_firstname()
    
    payload = {
        'login': login,
        'password': password,
        'firstName': first_name
    }
    
    # Создаем курьера без проверок
    response = requests.post(Urls.URL_courier_create, data=payload)
    
    # Получаем ID курьера через логин
    login_payload = {'login': login, 'password': password}
    login_response = requests.post(Urls.URL_courier_login, data=login_payload)
    
    if login_response.status_code == 200:
        courier_id = login_response.json()['id']
        return {
            'id': courier_id,
            'login': login,
            'password': password,
            'firstName': first_name
        }
    else:
        # Если не удалось получить ID, возвращаем None
        return None


@pytest.fixture
def cleanup_test_courier():
    """Фикстура для очистки тестового курьера"""
    # Создаем курьера для тестов
    create_payload = {
        'login': Data.valid_courier_data['login'],
        'password': Data.valid_courier_data['password'],
        'firstName': Data.valid_courier_data['firstName']
    }
    requests.post(Urls.URL_courier_create, data=create_payload)
    
    yield
    
    # После теста удаляем курьера
    login_response = requests.post(Urls.URL_courier_login, data=Data.valid_courier_data)
    if login_response.status_code == 200:
        courier_id = login_response.json()['id']
        requests.delete(f"{Urls.URL_courier_create}/{courier_id}")