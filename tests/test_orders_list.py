import requests
import allure
import pytest
from urls import Urls
from helpers import validate_order_structure


class TestOrdersListGet:

    @allure.title('Проверка получения списка заказов')
    def test_orders_list_get_success(self):
        response = requests.get(Urls.URL_orders_create)
        assert response.status_code == 200
        response_data = response.json()
        assert isinstance(response_data['orders'], list)

    @allure.title('Проверка базовой структуры ответа')
    def test_orders_list_basic_structure(self):
        response = requests.get(Urls.URL_orders_create)
        assert response.status_code == 200
        response_data = response.json()
        assert 'orders' in response_data
        assert isinstance(response_data['orders'], list)

    @allure.title('Проверка пагинации списка заказов')
    def test_orders_list_with_parameters(self):
        params = {'limit': 5, 'offset': 0}
        response = requests.get(Urls.URL_orders_create, params=params)
        assert response.status_code == 200
        response_data = response.json()
        assert 'orders' in response_data
        assert isinstance(response_data['orders'], list)


class TestOrdersListNonEmptyFeatures:
    """Тесты требующие непустой список заказов"""

    @allure.title('Проверка что заказы содержат поле id')
    def test_orders_list_has_id(self):
        response = requests.get(Urls.URL_orders_create)
        orders_list = response.json()['orders']
        assert orders_list, "Для выполнения тестов требуется непустой список заказов"
        assert 'id' in orders_list[0]

    @allure.title('Проверка полной структуры заказа')
    def test_orders_list_complete_structure(self):
        response = requests.get(Urls.URL_orders_create)
        orders_list = response.json()['orders']
        assert orders_list, "Для выполнения тестов требуется непустой список заказов"
        validate_order_structure(orders_list[0])