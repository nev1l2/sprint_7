import requests
import json
import allure
from urls import Urls


class OrderMethods:

    @allure.step('Создаем новый заказ')
    def post_create_order(self, payload):
        return requests.post(Urls.URL_orders_create, data=json.dumps(payload))

    @allure.step('Получаем список заказов')
    def get_orders_list(self):
        return requests.get(Urls.URL_orders_list)

    @allure.step('Принимаем заказ')
    def put_orders_accept(self, orders_id, courier_id):
        return requests.put(f'{Urls.URL_orders_accept}/{orders_id}?courierId={courier_id}')

    @allure.step('Получить заказ по его номеру')
    def get_orders_accept(self, orders_t):
        return requests.get(f'{Urls.URL_orders_track}{orders_t}')

