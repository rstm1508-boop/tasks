def number_sequence(start, end, even=True):
    """Генератор чисел: возвращает либо четные, либо нечетные числа."""
    if even:
        # Генерируем четные числа
        for num in range(start + start % 2, end + 1, 2):  # Учитываем стартовое число
            yield num
    else:
        # Генерируем нечетные числа
        for num in range(start + (not start % 2), end + 1, 2):  # Начинаем с ближайшего нечетного
            yield num

# Запрашиваем диапазон у пользователя
try:
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))
except ValueError:
    print("Ошибка ввода. Необходимо ввести целые числа.")
else:
    # Выбор типа последовательности
    choice = input("Выберите тип последовательности (четные / нечетные): ").strip().lower()
    
    if choice not in ['четные', 'нечетные']:
        print("Некорректный выбор. Выберите \"чётные\" или \"нечётные\".")
    elif choice == 'четные':
        result = list(number_sequence(start, end))
    else:
        result = list(number_sequence(start, end, even=False))
        
    print(f"Ваша последовательность: {result}")