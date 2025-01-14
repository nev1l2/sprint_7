import allure
import pytest


class TestLoginCourier:

    @allure.title('Проверяем авторизацию курьера ранее зарегистрированного.')
    def test_login_courier(self, courier_data, courier_methods):
        payload = courier_data[1]
        login_message = {"id":courier_data[0]}
        login = payload["login"]
        password = payload["password"]
        response = courier_methods.post_login_courier(login, password)
        assert response.status_code == 200 and response.json() == login_message

    @allure.title('Проверяем что невозможно авторизоваться незарегистрированным курьером.')
    def test_login_with_unregistered_courier(self, courier_methods):
        login = "unregistered_login",
        password = "unregistered_password"
        response = courier_methods.post_login_courier(login, password)
        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Проверяем что невозможно авторизоваться при отсутствии обязательных полей.')
    @pytest.mark.parametrize('empty_field_name', ["login", "password"])
    def test_login_courier_with_empty_field_login_or_password(self, courier_data, courier_methods, empty_field_name):
        payload = courier_data[1]
        payload[empty_field_name] = ''
        login = payload["login"]
        password = payload["password"]
        response = courier_methods.post_login_courier(login, password)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Проверяем что невозможно авторизоваться при отправке некорректных данных.')
    @pytest.mark.parametrize('field_name', ["login", "password"])
    def test_login_courier_with_incorrect_login_or_password(self, courier_data, courier_methods, field_name):
        payload = courier_data[1]
        payload[field_name] = 'incorrect_data'
        login = payload["login"]
        password = payload["password"]
        response = courier_methods.post_login_courier(login, password)
        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'