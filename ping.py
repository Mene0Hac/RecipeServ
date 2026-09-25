import requests

URL = "http://127.0.0.1:5000/"


while True:
    try:
        _ = input("№: ")
        if _ == "1":
            response = requests.get(URL+"get_all_users")
            print("Статус:", response.status_code)
        if _ == "2":
            response = requests.get(URL+"get_all_users")
            print("Статус:", response.status_code)
            print("Данные:", response.json())

    except requests.exceptions.ConnectionError:
        print("Ошибка: сервер не запущен или недоступен")

    except requests.exceptions.RequestException as e:
        print("Ошибка запроса:", e)