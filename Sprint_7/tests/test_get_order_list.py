import requests
import allure
import pytest
import sys
import os
from urls import Url

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from data import DataForOrder, StatusCode, TestData, ResponseBody, Flags


class TestGetOrdersList:

    @allure.title('Получение списка заказов')
    def test_orders_list_returns_array(self):
        with allure.step("Получить список заказов"):
            response = requests.get(f'{Url.MAIN_URL}{Url.GET_ORDER_LIST}')

        assert response.status_code == StatusCode.OK and Flags.SUCCESSFUL_GET_ORDER_LIST in response.json()

        orders = response.json()[Flags.SUCCESSFUL_GET_ORDER_LIST]
        assert isinstance(orders, list)

        # Проверка структуры заказов
        if orders:  # Если список не пустой
            first_order = orders[0]
        
            # Проверяем обязательные поля в заказе
            assert "id" in first_order, "В заказе должен быть ID"
            assert "track" in first_order, "В заказе должен быть track номер"
            assert "firstName" in first_order, "В заказе должно быть имя"
            assert "lastName" in first_order, "В заказе должна быть фамилия"
            assert "address" in first_order, "В заказе должен быть адрес"

            # Проверяем типы данных (допускаем None для строковых полей)
            assert isinstance(first_order["id"], int), "ID заказа должен быть числом"
            assert isinstance(first_order["track"], int), "Track номер должен быть числом"
        
            # Допускаем как строку, так и None для имени и фамилии
            assert first_order["firstName"] is None or isinstance(first_order["firstName"], str), "Имя должно быть строкой или null"
            assert first_order["lastName"] is None or isinstance(first_order["lastName"], str), "Фамилия должна быть строкой или null"
            assert first_order["address"] is None or isinstance(first_order["address"], str), "Адрес должен быть строкой или null"