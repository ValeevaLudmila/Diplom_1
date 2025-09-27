import requests
import allure
import pytest
from data import Url


class TestAcceptOrder:

    @allure.title('Успешное принятие заказа')
    def test_accept_order_success(self, create_courier):
        order_response = requests.post(f'{Url.MAIN_URL}{Url.POST_CREATING_ORDER}', json={
            "firstName": "Иван",
            "lastName": "Ульянов",
            "address": "Борисоглебская",
            "metroStation": 7,
            "phone": "+7 904 356 47 53",
            "rentTime": 1,
            "deliveryDate": "2025-09-27",
            "comment": "тест",
            "color": ["BLACK"]
        })
        order_track = order_response.json()["track"]
        order_id = requests.get(f'{Url.MAIN_URL}{Url.Get_ORDER_BY_NUMBER}?t={order_track}').json().get("order", {}).get("id")
        response = requests.put(f'{Url.MAIN_URL}{Url.ORDER_ACCEPT}{order_id}', params={"courierId": create_courier[4]})
        assert response.status_code == 200
        requests.put(f'{Url.MAIN_URL}{Url.ORDER_CANCEL}', params={"track": order_track})

    @pytest.mark.parametrize("scenario,order_id,courier_id,expected_status", [
        ("без id курьера", "real", "", 400),
        ("с несуществующим id курьера", "real", 999999, 404),
        ("без id заказа", "", "real", 400), # Баг: 404 вместо 400
        ("с несуществующим id заказа", 999999, "real", 404),
    ])
    
    @allure.title('Ошибка при принятии заказа: {scenario}')
    def test_accept_order_errors_parametrized(self, create_courier, scenario, order_id, courier_id, expected_status):
        if order_id == "real":
            order_response = requests.post(f'{Url.MAIN_URL}{Url.POST_CREATING_ORDER}', json={
                "firstName": "Тест", "lastName": "Тестов", "address": "Адрес",
                "metroStation": 4, "phone": "+7 800 355 35 35", "rentTime": 1,
                "deliveryDate": "2025-01-01", "comment": "тест", "color": ["BLACK"]
            })
            real_order_id = requests.get(f'{Url.MAIN_URL}{Url.Get_ORDER_BY_NUMBER}?t={order_response.json()["track"]}').json().get("order", {}).get("id")
            used_order_id = real_order_id
            order_track = order_response.json()["track"]
        else:
            used_order_id = order_id
            order_track = None
        if courier_id == "real":
            used_courier_id = create_courier[4]
        else:
            used_courier_id = courier_id
        params = {}
        if used_courier_id != "":
            params["courierId"] = used_courier_id
        response = requests.put(f'{Url.MAIN_URL}{Url.ORDER_ACCEPT}{used_order_id}', params=params)
        assert response.status_code == expected_status
        if order_track:
            requests.put(f'{Url.MAIN_URL}{Url.ORDER_CANCEL}', params={"track": order_track})