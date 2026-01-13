import threading
import time

# Функция отправки уведомления
def send_notification(user, delay):
    print(f'Отправляю уведомление {user}')
    # Имитация задержки отправляя уведомления
    time.sleep(delay)
    print(f'Уведомление для {user} успешно отправлено')

if __name__ == "__main__":
    users = [
        ("Alice", 2),
        ("Bob", 3),
        ("Charlie", 1),
        ("Diana", 4)
    ]
    
    threads = []
    
    for user, delay in users:
        thread = threading.Thread(target=send_notification, args=(user, delay))
        threads.append(thread)
        thread.start()
        
    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()