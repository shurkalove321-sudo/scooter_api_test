# test_create_order.py
import time
from sender_stand_request import post_new_order, get_order_by_track
from data import order_body

def test_create_and_get_order():
    # Создание заказа
    create_response = post_new_order(order_body)
    assert create_response.status_code == 201, "Ошибка при создании заказа"

    # Получаем трек заказа
    track_number = create_response.json()["track"]

    # Пауза, чтобы сервер успел зарегистрировать заказ
    time.sleep(1)

    # Получение заказа по треку
    get_response = get_order_by_track(track_number)
    assert get_response.status_code == 200, "Ошибка при получении заказа по треку"

    order = get_response.json()["order"]
    assert order["track"] == track_number

