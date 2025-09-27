import requests
import allure
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from data import Url, Flags


class TestGetOrdersList:

    @allure.title('Получение списка заказов')
    def test_orders_list_returns_array(self):
        response = requests.get(f'{Url.MAIN_URL}{Url.GET_ORDER_LIST}')
        
        assert response.status_code == 200 and Flags.SUCCESSFUL_GET_ORDER_LIST in response.json()
        
        orders = response.json()[Flags.SUCCESSFUL_GET_ORDER_LIST]
        assert isinstance(orders, list)