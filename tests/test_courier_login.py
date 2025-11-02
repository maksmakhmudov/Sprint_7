import requests
import allure
import pytest
from data import Data
from urls import Urls
from helpers import create_random_login, create_random_password


class TestCourierLogin:

    @allure.title('Проверка успешной аутентификации курьера')
    def test_courier_login_success(self):
        # Сначала создаем курьера
        create_response = requests.post(Urls.URL_courier_create, data=Data.valid_courier_data)
        # Если курьер уже существует (409) - это нормально
        assert create_response.status_code in [201, 409]
        
        # Теперь логинимся
        response = requests.post(Urls.URL_courier_login, data=Data.valid_courier_data)
        
        assert response.status_code == 200
        response_data = response.json()
        assert 'id' in response_data
        assert isinstance(response_data['id'], int)
        
        # Очистка - получаем ID и удаляем курьера
        courier_id = response_data['id']
        delete_response = requests.delete(f"{Urls.URL_courier_create}/{courier_id}")
        assert delete_response.status_code in [200, 204]

    @allure.title('Проверка ошибки аутентификации при невалидных данных')
    @pytest.mark.parametrize('nonexistent_credentials', [
        {'login': create_random_login(), 'password': create_random_password()},
        {'login': Data.valid_login, 'password': 'wrong_password_123456'}
    ])
    def test_courier_login_nonexistent_data_not_found(self, nonexistent_credentials):
        response = requests.post(Urls.URL_courier_login, data=nonexistent_credentials)
        
        assert response.status_code == 404
        assert response.json().get('message') == Data.Messages.ACCOUNT_NOT_FOUND

    @allure.title('Проверка ошибки аутентификации с пустыми полями')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password()},
        {'login': Data.valid_login, 'password': ''}
    ])
    def test_courier_login_empty_credentials_bad_request(self, empty_credentials):
        response = requests.post(Urls.URL_courier_login, data=empty_credentials)
        
        assert response.status_code == 400
        assert response.json().get('message') == Data.Messages.NOT_ENOUGH_DATA_FOR_LOGIN