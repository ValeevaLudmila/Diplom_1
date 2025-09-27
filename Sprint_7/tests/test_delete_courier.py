import requests
import allure
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from data import Url, ResponseBody
from generators import login_generator, password_generator, name_generator

class TestDeleteCourier:
    
    @allure.title('Успешное удаление курьера')
    def test_delete_courier(self, create_courier):
        login_response = requests.post(
            f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', 
            json=create_courier[1]
        )
        courier_id = login_response.json()["id"]
        response = requests.delete(f'{Url.MAIN_URL}{Url.COURIER_DELETE}{courier_id}')
        
        assert response.status_code == 200 and response.json() == {"ok": True}

    @allure.title('Ошибка при запросе с несуществующим id')  # Баг: 500 вместо 404
    def test_delete_nonexistent_courier_returns_error(self):
        nonexistent_id = 9999999999999999999999
        response = requests.delete(f'{Url.MAIN_URL}{Url.COURIER_DELETE}{nonexistent_id}')
        
        assert response.status_code == 404 and response.json() == ResponseBody.COURIER_ACCOUNT_NOT_FOUND

    @allure.title('Ошибка при запросе без id') # Баг: 404 вместо 400
    def test_delete_courier_without_id_returns_error(self):
        response = requests.delete(f'{Url.MAIN_URL}{Url.COURIER_DELETE}')
        
        assert response.status_code == 400 and "message" in response.json()