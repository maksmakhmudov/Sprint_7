import requests
import allure
import pytest
from urls import Urls


class TestOrdersListGet:

    @allure.title('Проверка получения списка заказов')
    @allure.description('Проверяются код и тело ответа.')
    def test_orders_list_get_success(self):
        response = requests.get(Urls.URL_orders_create)
        
        # Проверяем статус код ответа
        assert response.status_code == 200
        
        # Проверяем что ответ содержит список заказов
        response_data = response.json()
        assert isinstance(response_data['orders'], list)
        
        # Проверяем что первый заказ содержит поле 'id' (если список не пустой)
        if response_data['orders']:
            assert 'id' in response_data['orders'][0]

    @allure.title('Проверка структуры ответа списка заказов')
    @allure.description('Проверяется что ответ содержит все необходимые поля')
    def test_orders_list_structure(self):
        response = requests.get(Urls.URL_orders_create)
        
        assert response.status_code == 200
        
        response_data = response.json()
        
        # Проверяем базовую структуру ответа
        assert 'orders' in response_data
        assert isinstance(response_data['orders'], list)
        
        # Если есть заказы, проверяем структуру первого
        if response_data['orders']:
            first_order = response_data['orders'][0]
            # Проверяем основные поля заказа
            expected_fields = ['id', 'firstName', 'lastName', 'address', 'metroStation', 
                             'phone', 'rentTime', 'deliveryDate', 'track', 'color']
            
            for field in expected_fields:
                assert field in first_order, f"В заказе отсутствует поле '{field}'"

    @allure.title('Проверка пагинации списка заказов')
    @allure.description('Проверяется работа с параметрами limit и offset')
    def test_orders_list_with_parameters(self):
        # Тестируем с параметрами limit и offset
        params = {'limit': 5, 'offset': 0}
        response = requests.get(Urls.URL_orders_create, params=params)
        
        assert response.status_code == 200
        
        response_data = response.json()
        assert 'orders' in response_data
        assert isinstance(response_data['orders'], list)