import allure


class TestOrdersList:
    @allure.title('Получаем список заказов')
    def test_get_orders_list(self, order_methods):
        response = order_methods.get_orders_list()
        assert response.status_code == 200 and "orders" in response.json()