import allure

from urls import Urls
import requests
from helpers import generate_random_string


class CourierMethods:
    @allure.step('Генерируем логин, пароль и имя курьера')
    def courier_data_generation(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        return {
            "login": login,
            "password": password,
            "first_name": first_name
        }

    @allure.step('Регистрируем курьера')
    def post_registration_new_courier(self, payload):
        return requests.post(Urls.URL_courier_create, data=payload)

    @allure.step('Авторизация курьера')
    def post_login_courier(self, login, password):
        payload = {
            "login": login,
            "password": password,
        }
        return requests.post(Urls.URL_courier_login, data=payload)

    @allure.step('Удаляем курьера по id')
    def delete_courier(self, courier_id):
        return requests.delete(f'{Urls.URL_courier_delete}/{courier_id}')