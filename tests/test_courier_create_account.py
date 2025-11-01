# test_courier_create.py
import requests
import allure
import pytest
from data import Data
from urls import Urls
from helpers import create_random_login, create_random_password, create_random_firstname


class TestCourierCreate:

    @allure.title('Проверка успешного создания аккаунта курьера с валидными данными')
    def test_create_courier_account_success(self, cleanup_courier):
        payload = {
            'login': create_random_login(),
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }
        response = requests.post(Urls.URL_courier_create, data=payload)
        
        # Парсим и проверяем ответ
        assert response.status_code == 201
        
        response_data = response.json()
        assert 'ok' in response_data
        assert response_data['ok'] is True
        
        # Получаем ID созданного курьера для очистки
        login_payload = {'login': payload['login'], 'password': payload['password']}
        login_response = requests.post(Urls.URL_courier_login, data=login_payload)
        assert login_response.status_code == 200
        courier_id = login_response.json()['id']
        cleanup_courier[0].append(courier_id)

    @allure.title('Проверка получения ошибки при повторном использовании логина')
    def test_create_courier_account_login_taken_conflict(self, cleanup_courier, create_test_courier):
        # Используем фикстуру для создания первого курьера
        existing_courier = create_test_courier
        # Проверяем что курьер создан успешно
        assert existing_courier is not None
        cleanup_courier[0].append(existing_courier['id'])
        
        # Пытаемся создать второго курьера с тем же логином
        payload = {
            'login': existing_courier['login'],
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }
        response = requests.post(Urls.URL_courier_create, data=payload)
        
        assert response.status_code == 409
        response_data = response.json()
        assert 'message' in response_data
        assert response_data['message'] == Data.Messages.LOGIN_ALREADY_EXISTS