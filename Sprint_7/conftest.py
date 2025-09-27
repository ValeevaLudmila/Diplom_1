import pytest
import requests
import generators
from data import Url


@pytest.fixture
def create_courier():
    name = generators.name_generator()
    login = generators.login_generator()
    password = generators.password_generator()
    create_courier_body = {'login': login, 'password': password, 'firstName': name}
    login_courier_body = {'login': login, 'password': password}
    requests.post(f'{Url.MAIN_URL}{Url.CREATING_COURIER}', json=create_courier_body)
    login_courier = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=login_courier_body)
    courier_id = login_courier.json()["id"]
    yield [create_courier_body, login_courier_body, login, password, courier_id]
    requests.delete(f'{Url.MAIN_URL}{Url.COURIER_DELETE}{courier_id}')


@pytest.fixture
def generate_courier_data():
    name = generators.name_generator()
    login = generators.login_generator()
    password = generators.password_generator()
    creation_courier_body = {'login': login, 'password': password, 'firstName': name}
    login_courier_body = {'login': login, 'password': password}
    yield [creation_courier_body, login_courier_body]
    login_courier = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=login_courier_body)
    requests.delete(f'{Url.MAIN_URL}{Url.COURIER_DELETE}{login_courier.json()["id"]}')