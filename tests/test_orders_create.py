import requests
import allure
import pytest
import json
from data import Data
from urls import Urls


class TestOrderCreate:

    @allure.title('Проверка создания заказа с разными параметрами цвета: {color_case}')
    @allure.description('Согласно требованиям, система должна позволять указать в заказе один цвет самоката, выбрать '
                        'сразу оба или не указывать совсем. Проверяются код и тело ответа.')
    @pytest.mark.parametrize('order_data, color_case', [
        (Data.order_data_grey_1, "серый цвет"),
        (Data.order_data_black_2, "черный цвет"), 
        (Data.order_data_two_colors_3, "оба цвета"),
        (Data.order_data_no_colors_4, "цвет не указан")
    ])
    def test_order_create_color_parametrize_success(self, order_data, color_case):
        # Подготовка данных
        order_data_json = json.dumps(order_data)
        headers = {'Content-Type': 'application/json'}
        
        # Выполнение запроса
        response = requests.post(Urls.URL_orders_create, data=order_data_json, headers=headers, timeout=5)
        
        # Проверки
        assert response.status_code == 201, (
            f"Для случая '{color_case}' ожидался статус 201, получен {response.status_code}"
        )
        
        response_data = response.json()
        assert 'track' in response_data, (
            f"Для случая '{color_case}' в ответе отсутствует поле 'track'"
        )
        assert isinstance(response_data['track'], int), (
            f"Для случая '{color_case}' поле 'track' должно быть числом, получен {type(response_data['track'])}"
        )
        assert response_data['track'] > 0, (
            f"Для случая '{color_case}' track должен быть положительным числом"
        )