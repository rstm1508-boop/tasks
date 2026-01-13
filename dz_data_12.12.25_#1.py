import time


def log_action(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__}: выполнено за {end_time-start_time:.4f} сек.")
        return result
    return wrapper


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.deleted_tasks = []  

    @log_action
    def add_task(self, task_text):
        """Добавляет новую задачу"""
        if not task_text.strip():
            raise ValueError("Неверный ввод задачи")
        self.tasks.append(task_text)
        print("Задача добавлена.")
    
    @log_action
    def show_tasks(self):
        """Показывает список текущих задач"""
        if not self.tasks:
            print("Список задач пуст.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    @log_action
    def complete_task(self, index):
        """Выполняет задачу, удаляя её из списка"""
        try:
            removed_task = self.tasks.pop(index - 1)
            self.deleted_tasks.append(removed_task)
            print("Задача выполнена.")
        except IndexError:
            print("Неверный номер задачи!")
        
    @log_action
    def undo_last_change(self):
        """Отменяет последнее действие (восстанавливает удалённую задачу)"""
        if not self.deleted_tasks:
            print("Нет действий для отмены.")
        else:
            restored_task = self.deleted_tasks.pop()
            self.tasks.append(restored_task)
            print("Последняя задача восстановлена.")
            
    def run(self):
        while True:
            command = input("\nВведите команду (add/show/complete/undo/exit): ").strip().lower()
            if command == 'add':
                task_text = input("Введите текст задачи: ")
                self.add_task(task_text)
            elif command == 'show':
                self.show_tasks()
            elif command == 'complete':
                index = int(input("Введите номер задачи для выполнения: "))
                self.complete_task(index)
            elif command == 'undo':
                self.undo_last_change()
            elif command == 'exit':
                print("Программа завершена.")
                break
            else:
                print("Ошибка: неизвестная команда.")
                
if __name__ == "__main__":
    manager = TaskManager()
    manager.run()