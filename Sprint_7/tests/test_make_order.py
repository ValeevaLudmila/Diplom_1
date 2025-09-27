import requests
import allure
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from data import Url, DataForOrder, ResponseBody


class TestOrderCreation:

    @pytest.mark.parametrize("color_data", [
        ["BLACK"], ["GREY"], ["BLACK", "GREY"], [], None
    ])
    @allure.title('Создание заказа с разными цветами')
    def test_create_order_with_colors(self, color_data):
        order_data = DataForOrder.order_data.copy()
        
        if color_data is None:
            del order_data["color"]
        else:
            order_data["color"] = color_data
        response = requests.post(f'{Url.MAIN_URL}{Url.POST_CREATING_ORDER}', json=order_data)
    
        assert response.status_code == 201 and "track" in response.json()
        
        track_number = response.json()["track"]
        requests.put(f'{Url.MAIN_URL}{Url.ORDER_CANCEL}', json={"track": track_number})