import requests

URL = "http://127.0.0.1:5000/"

try:
    response = requests.get(URL+"get_all_users")
    print("Статус:", response.status_code)
    for row in response.json():
        print(f"ID: {row['id']}, Имя: {row['name']}, Возраст: {row['age']}"+"\n")

except requests.exceptions.ConnectionError:
    print("Ошибка: сервер не запущен или недоступен")

except requests.exceptions.RequestException as e:
    print("Ошибка запроса:", e)