# Scooter API Test

##  Описание
Я сделала автотест для проверки API Яндекс.Самокат:
- создаётся заказ через POST-запрос;
- по треку заказа можно получить данные GET-запросом.

Тест написан на **Python + Pytest**.

---

##  Структура проекта
- `configuration.py` — базовый URL и пути API.
- `data.py` — тестовые данные (тело заказа).
- `sender_stand_request.py` — функции для запросов.
- `test_create_order.py` — автотест (pytest).
- `.gitignore` — игнор временных файлов и кэша.
- `README.md` — описание проекта.

---

##  Установка зависимостей
```bash
python -m pip install --upgrade pip
pip install requests pytest
