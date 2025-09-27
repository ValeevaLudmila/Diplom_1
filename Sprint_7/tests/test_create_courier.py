import requests
import allure
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from data import Url, ResponseBody, DataForRegistration
from generators import login_generator, password_generator, name_generator


class TestsCreateNewCourier:

    @allure.title('Создать нового курьера')
    def test_creation_courier_success(self, generate_courier_data):
        registration = requests.post(f'{Url.MAIN_URL}{Url.CREATING_COURIER}', json=generate_courier_data[0])
        assert registration.status_code == 201 and (registration.json() == ResponseBody.COURIER_CREATION_SUCCESS)

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_duplicate_courier_returns_error(self, create_courier):
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATING_COURIER}', json=create_courier[0])
        assert response.status_code == 409, f"Ожидалась ошибка 409, получен {response.status_code}"
        assert response.json() == ResponseBody.COURIER_NAME_ALREADY_EXIST

    @allure.title('Eсли одного из полей нет, запрос возвращает ошибку')
    @pytest.mark.parametrize('data_setup', DataForRegistration.reg_data)
    def test_error_occurs_if_one_of_the_fields_is_missing(self, data_setup):
        incomplete_data = data_setup.copy()
        del incomplete_data['login']
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATING_COURIER}', json=incomplete_data)
        assert response.status_code == 400
        assert response.json()['message'] == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA['message']