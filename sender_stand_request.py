#Довиденко Александра 34-я когорта - Финальный проект. Инженер по тестированию плюс
import requests
from configuration import URL_SERVICE, CREATE_ORDER_PATH, GET_ORDER_BY_TRACK_PATH

def post_new_order(order_data):
    """Создать новый заказ"""
    response = requests.post(
        f"{URL_SERVICE}{CREATE_ORDER_PATH}",
        json=order_data,
        headers={"Content-Type": "application/json"}
    )
    return response

def get_order_by_track(track):
    """Получить заказ по треку"""
    response = requests.get(f"{URL_SERVICE}{GET_ORDER_BY_TRACK_PATH}?t={track}")
    return response

