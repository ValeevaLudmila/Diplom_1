import requests
import allure
from data import Url


class TestGetOrderByTrack:

    @allure.title('Успешное получение заказа')
    def test_get_order_success(self):
        order_response = requests.post(f'{Url.MAIN_URL}{Url.POST_CREATING_ORDER}', json={
            "firstName": "Тест",
            "lastName": "Тестов",
            "address": "Адрес",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 1,
            "deliveryDate": "2025-01-01",
            "comment": "тест",
            "color": ["BLACK"]
        })
        track = order_response.json()["track"]
        response = requests.get(f'{Url.MAIN_URL}{Url.Get_ORDER_BY_NUMBER}?t={track}')
        assert response.status_code == 200 and "order" in response.json()
        requests.put(f'{Url.MAIN_URL}{Url.ORDER_CANCEL}', params={"track": track})

    @allure.title('Ошибка при отсутствии номера')
    def test_get_order_without_track(self):
        response = requests.get(f'{Url.MAIN_URL}{Url.Get_ORDER_BY_NUMBER}')
        assert response.status_code == 400

    @allure.title('Ошибка при несуществующем номере')
    def test_get_order_nonexistent_track(self):
        response = requests.get(f'{Url.MAIN_URL}{Url.Get_ORDER_BY_NUMBER}?t=999999')
        assert response.status_code == 404