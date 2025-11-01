# test_courier_login.py
import requests
import allure
import pytest
from data import Data
from urls import Urls
from helpers import create_random_login, create_random_password


class TestCourierLogin:

    @allure.title('Проверка успешной аутентификации курьера')
    def test_courier_login_success(self, cleanup_test_courier):
        response = requests.post(Urls.URL_courier_login, data=Data.valid_courier_data)
        
        assert response.status_code == 200
        response_data = response.json()
        assert 'id' in response_data
        assert isinstance(response_data['id'], int)

    @allure.title('Проверка ошибки аутентификации при невалидных данных')
    @pytest.mark.parametrize('nonexistent_credentials', [
        {'login': create_random_login(), 'password': create_random_password()},
        {'login': Data.valid_login, 'password': 'wrong_password_123456'}
    ])
    def test_courier_login_nonexistent_data_not_found(self, nonexistent_credentials):
        response = requests.post(Urls.URL_courier_login, data=nonexistent_credentials)
        
        assert response.status_code == 404
        assert response.json().get('message') == 'Учетная запись не найдена'

    @allure.title('Проверка ошибки аутентификации с пустыми полями')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password()},
        {'login': Data.valid_login, 'password': ''}
    ])
    def test_courier_login_empty_credentials_bad_request(self, empty_credentials):
        response = requests.post(Urls.URL_courier_login, data=empty_credentials)
        
        assert response.status_code == 400
        assert response.json().get('message') == 'Недостаточно данных для входа'