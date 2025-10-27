import requests
import allure
import pytest
from data import Data
from urls import Urls
from helpers import create_random_login, create_random_password


class TestCourierLogin:

    @allure.title('Проверка успешной аутентификации курьера при вводе валидных данных')
    @allure.description('Happy path. Проверяются код и тело ответа.')
    def test_courier_login_success(self):
        # создаем курьера, чтобы он существовал в системе
        create_payload = {
            'login': Data.valid_courier_data['login'],
            'password': Data.valid_courier_data['password'],
            'firstName': Data.valid_courier_data['firstName']
        }
        requests.post(Urls.URL_courier_create, data=create_payload)
        
        # выполняем логин
        response = requests.post(Urls.URL_courier_login, data=Data.valid_courier_data)
        
        # проверяем статус 200 и поле 'id'
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Проверка получения ошибки аутентификации курьера при вводе невалидных данных')
    @allure.description('В тест по очереди передаются наборы данных с несуществующим логином или неверным паролем. '
                        'Проверяются код и тело ответа.')
    @pytest.mark.parametrize('nonexistent_credentials', [
        {'login': create_random_login(), 'password': create_random_password()},
        {'login': Data.valid_login, 'password': 'wrong_password_123456'}
    ])
    def test_courier_login_nonexistent_data_not_found(self, nonexistent_credentials):
        response = requests.post(Urls.URL_courier_login, data=nonexistent_credentials)
        
        # проверяем статус и сообщение через get()
        assert response.status_code == 404
        assert response.json().get('message') == 'Учетная запись не найдена'

    @allure.title('Проверка получения ошибки аутентификации курьера с пустым полем логина или пароля')
    @allure.description('В тест по очереди передаются наборы данных с пустым логином или паролем. '
                        'Проверяются код и тело ответа.')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password()},
        {'login': Data.valid_login, 'password': ''}
    ])
    def test_courier_login_empty_credentials_bad_request(self, empty_credentials):
        response = requests.post(Urls.URL_courier_login, data=empty_credentials)
        
        # проверяем статус и сообщение через get()
        assert response.status_code == 400
        assert response.json().get('message') == 'Недостаточно данных для входа'