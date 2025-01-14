import allure

from methods.courier_methods import CourierMethods


class TestDeleteCourier:

    @allure.title('Проверяем что курьера можно удалить указав id')
    def test_delete_courier(self, courier_data):
        payload = CourierMethods().courier_data_generation()
        creation_response = CourierMethods().post_registration_new_courier(payload)
        login = payload['login']
        password = payload['password']
        courier_id = CourierMethods().post_login_courier(login, password).json()['id']
        response = CourierMethods().delete_courier(courier_id)
        assert creation_response.status_code == 201 and response.status_code == 200 and response.text == '{"ok":true}'

    @allure.title('Проверяем что выводится ошибка при удалении курьера не указав id')
    def test_delete_courier_without_id(self):
        courier_id = ''
        response = CourierMethods().delete_courier(courier_id)
        assert response.status_code == 404 and response.text == '{"code":404,"message":"Not Found."}'

    @allure.title('Проверяем что выводится ошибка при удалении курьера указав несуществующий id')
    def test_delete_courier_with_non_existent_id(self):
        courier_id = 1242423243
        response = CourierMethods().delete_courier(courier_id)
        assert response.status_code == 404 and response.text == '{"code":404,"message":"Курьера с таким id нет."}'