
import requests # библиотека для работы с API
import time 

BASE_URL = "https://db4c1c27-599a-46b9-a50b-61859504dd63.serverhub.praktikum-services.ru"

# Создаем заказ 
create_response = requests.post(
    f"{BASE_URL}/api/v1/orders",
    json={
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": "4",
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-09-12",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }
)

# Получаем трек заказа
track = create_response.json()["track"]
print("Заказ создан. Трек:", track)

# Пауза для надёжности 
time.sleep(1)  # 1 секунда для обработки запроса, чтобы не упал случайно

# Получаем заказ по треку 
get_response = requests.get(f"{BASE_URL}/api/v1/orders/track?t={track}")

# Проверка кода ответа 
if get_response.status_code == 200:
    print("Тест пройден! Код ответа 200")
else:
    print("Ошибка! Код ответа:", get_response.status_code)
    print("Ответ сервера:", get_response.text)