import allure

from methods.courier_methods import CourierMethods


class TestOrderAccept:

    @allure.title('Проверяем что заказ можно принять')
    def test_orders_accept(self, order_methods):
        payload = CourierMethods().courier_data_generation()
        CourierMethods().post_registration_new_courier(payload)
        login = payload['login']
        password = payload['password']
        courier_id = CourierMethods().post_login_courier(login, password).json()['id']
        order_id= order_methods.get_orders_list().json()['orders'][0]['id']

        response = order_methods.put_orders_accept(order_id, courier_id)
        assert response.status_code == 200 and response.text == '{"ok":true}'


