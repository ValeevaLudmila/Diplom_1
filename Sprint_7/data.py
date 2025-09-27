import generators

class Url:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru/'
    CREATING_COURIER = '/api/v1/courier'
    COURIER_LOGIN = '/api/v1/courier/login'
    COURIER_DELETE = '/api/v1/courier/'
    GET_ORDER_LIST = '/api/v1/orders'
    POST_CREATING_ORDER = '/api/v1/orders'
    Get_ORDER_BY_NUMBER = '/api/v1/orders/track'
    ORDER_CANCEL = '/api/v1/orders/cancel'
    ORDER_ACCEPT = '/api/v1/orders/accept/'


class DataForOrder:
    order_data = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}
    

class DataForRegistration:
    reg_data = [
        {'login': generators.login_generator(), 'firstName': generators.name_generator(), 'password': generators.password_generator()},
    ]


class ResponseBody:
    COURIER_CREATION_SUCCESS = {'ok': True}
    ORDER_ACCEPT_SUCCESS = {'ok': True}
    COURIER_NAME_ALREADY_EXIST = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
    COURIER_REGISTRATION_NOT_ENOUGH_DATA = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
    COURIER_ACCOUNT_NOT_FOUND = {'code': 404, 'message': 'Учетная запись не найдена'}
    COURIER_LOGIN_NOT_ENOUCH_DATA = {'code': 400, 'message': 'Недостаточно данных для входа'}


class Flags:
    SUCESSFUL_ORDER_CREATION = 'track'
    SUCCESSFUL_GET_ORDER_LIST = 'orders'