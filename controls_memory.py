import psutil
import requests

# Задайте API URL для отправки HTTP-запроса
api_url = 'http://example.com/alarm'

# Задайте предельное значение использования памяти (в процентах)
memory_threshold = 90

def check_memory_usage():
    # Получаем информацию о потреблении памяти
    memory_percent = psutil.virtual_memory().percent

    # Если использование памяти превышает предельное значение, отправляем HTTP-запрос на API
    if memory_percent > memory_threshold:
        payload = {'message': 'High memory usage!'}
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            print('Alarm sent successfully!')
        else:
            print('Failed to send alarm.')

# Вызываем функцию для проверки использования памяти
check_memory_usage()