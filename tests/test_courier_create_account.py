import requests
import allure
import pytest
from data import Data
from urls import Urls
from helpers import create_random_login, create_random_password, create_random_firstname


@pytest.fixture
def cleanup_courier():
    """Фикстура для очистки созданного курьера после теста"""
    courier_ids = []  # Список для хранения ID созданных курьеров
    courier_logins = []  # Список для хранения логинов созданных курьеров
    
    yield courier_ids, courier_logins
    
    # После выполнения теста удаляем всех созданных курьеров
    for courier_id in courier_ids:
        if courier_id:
            delete_response = requests.delete(f"{Urls.URL_courier_create}/{courier_id}")
            assert delete_response.status_code in [200, 204, 404], f"Не удалось удалить курьера {courier_id}"


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
    
    response = requests.post(Urls.URL_courier_create, data=payload)
    assert response.status_code == 201
    
    # Получаем ID курьера через логин
    login_payload = {'login': login, 'password': password}
    login_response = requests.post(Urls.URL_courier_login, data=login_payload)
    assert login_response.status_code == 200
    
    courier_id = login_response.json()['id']
    
    return {
        'id': courier_id,
        'login': login,
        'password': password,
        'firstName': first_name
    }


class TestCourierCreate:

    @allure.title('Проверка успешного создания аккаунта курьера с валидными данными')
    @allure.description('Happy path. Проверяются код и тело ответа.')
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
        assert 'ok' in response_data, "В ответе отсутствует поле 'ok'"
        assert response_data['ok'] is True, "Поле 'ok' должно быть True"
        
        # Получаем ID созданного курьера для очистки
        login_payload = {'login': payload['login'], 'password': payload['password']}
        login_response = requests.post(Urls.URL_courier_login, data=login_payload)
        if login_response.status_code == 200:
            courier_id = login_response.json()['id']
            cleanup_courier[0].append(courier_id)

    @allure.title('Проверка получения ошибки при повторном использовании логина для создания курьера')
    @allure.description('Проверяются код и тело ответа.')
    def test_create_courier_account_login_taken_conflict(self, cleanup_courier, create_test_courier):
        # Используем фикстуру для создания первого курьера
        existing_courier = create_test_courier
        cleanup_courier[0].append(existing_courier['id'])
        
        # Пытаемся создать второго курьера с тем же логином
        payload = {
            'login': existing_courier['login'],
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }
        response = requests.post(Urls.URL_courier_create, data=payload)
        
        # Парсим и проверяем ответ с ошибкой
        assert response.status_code == 409
        
        response_data = response.json()
        assert 'message' in response_data, "В ответе об ошибке отсутствует поле 'message'"
        assert response_data['message'] == Data.Messages.LOGIN_ALREADY_EXISTS

    @allure.title('Проверка получения ошибки при создании курьера с незаполненными обязательными полями')
    @allure.description('В тест по очереди передаются наборы данных с пустым логином или паролем. '
                        'Проверяются код и тело ответа.')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password(), 'firstName': create_random_firstname()},
        {'login': create_random_login(), 'password': '', 'firstName': create_random_firstname()}
    ])
    def test_create_courier_account_with_empty_required_fields(self, empty_credentials):
        # Для негативных тестов очистка не требуется, так как курьер не создается
        response = requests.post(Urls.URL_courier_create, data=empty_credentials)
        
        # Парсим и проверяем ответ с ошибкой
        assert response.status_code == 400
        
        response_data = response.json()
        assert 'message' in response_data, "В ответе об ошибке отсутствует поле 'message'"
        assert response_data['message'] == Data.Messages.NOT_ENOUGH_DATA_FOR_CREATE

    @allure.title('Проверка создания курьера без указания имени')
    @allure.description('Проверяется что имя не является обязательным полем')
    def test_create_courier_account_without_firstname_success(self, cleanup_courier):
        payload = {
            'login': create_random_login(),
            'password': create_random_password(),
            'firstName': ''
        }
        response = requests.post(Urls.URL_courier_create, data=payload)
        
        # Парсим и проверяем ответ
        assert response.status_code == 201
        
        response_data = response.json()
        assert 'ok' in response_data, "В ответе отсутствует поле 'ok'"
        assert response_data['ok'] is True, "Поле 'ok' должно быть True"
        
        # Получаем ID созданного курьера для очистки
        login_payload = {'login': payload['login'], 'password': payload['password']}
        login_response = requests.post(Urls.URL_courier_login, data=login_payload)
        if login_response.status_code == 200:
            courier_id = login_response.json()['id']
            cleanup_courier[0].append(courier_id)

    @allure.title('Проверка создания курьера с минимальными данными')
    @allure.description('Проверяется создание курьера только с логином и паролем')
    def test_create_courier_account_minimal_data_success(self, cleanup_courier):
        payload = {
            'login': create_random_login(),
            'password': create_random_password()
        }
        response = requests.post(Urls.URL_courier_create, data=payload)
        
        # Парсим и проверяем ответ
        assert response.status_code == 201
        
        response_data = response.json()
        assert 'ok' in response_data, "В ответе отсутствует поле 'ok'"
        assert response_data['ok'] is True, "Поле 'ok' должно быть True"
        
        # Получаем ID созданного курьера для очистки
        login_payload = {'login': payload['login'], 'password': payload['password']}
        login_response = requests.post(Urls.URL_courier_login, data=login_payload)
        if login_response.status_code == 200:
            courier_id = login_response.json()['id']
            cleanup_courier[0].append(courier_id)

    @allure.title('Проверка структуры ответа при успешном создании курьера')
    @allure.description('Проверяется что ответ содержит все необходимые поля')
    def test_create_courier_response_structure(self, cleanup_courier):
        payload = {
            'login': create_random_login(),
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }
        response = requests.post(Urls.URL_courier_create, data=payload)
        
        assert response.status_code == 201
        
        response_data = response.json()
        
        # Проверяем все возможные поля в успешном ответе
        assert 'ok' in response_data
        assert response_data['ok'] is True
        
        # Получаем ID созданного курьера для очистки
        login_payload = {'login': payload['login'], 'password': payload['password']}
        login_response = requests.post(Urls.URL_courier_login, data=login_payload)
        if login_response.status_code == 200:
            courier_id = login_response.json()['id']
            cleanup_courier[0].append(courier_id)