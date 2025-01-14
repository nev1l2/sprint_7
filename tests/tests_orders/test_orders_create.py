import allure
import pytest
from data import CreateOrder


class TestCreateOrder:
    @allure.title('Проверяем создание заказа с разными цветами')
    @pytest.mark.parametrize('color', (['BLACK'], ['GREY'], ['BLACK', 'GREY'], []))
    def test_create_order_with_different_color(self, order_methods, color):
        payload = CreateOrder.order_data
        payload["color"] = color
        response = order_methods.post_create_order(payload)
        assert response.status_code == 201 and 'track' in response.json()