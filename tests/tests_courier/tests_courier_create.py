import pytest
import allure


class TestCreateCourier:

    @allure.title('Проверяем что курьера можно создать')
    def test_create_courier(self, courier_data):
        response = courier_data[2]
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Проверяем, что нельзя создать двух одинаковых курьеров')
    def test_create_two_identical_couriers(self, courier_methods, courier_data):
        payload = courier_data[1]
        response = courier_methods.post_registration_new_courier(payload)
        assert (response.status_code == 409 and response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.')

    @allure.title('Проверяем что нельзя зарегистрировать курьера без заполнения обязательных полей')
    @pytest.mark.parametrize('empty_field_name', ["login", "password"])
    def test_create_courier_with_empty_field_login_or_password(self, courier_methods, empty_field_name):
        payload = courier_methods.courier_data_generation()
        payload[empty_field_name] = ''
        response = courier_methods.post_registration_new_courier(payload)
        assert (response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для создания учетной записи')

