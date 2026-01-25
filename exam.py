class Item:
    def __init__(self, item_id, title, year):
        self.item_id = item_id
        self.title = title
        self.year = year


class Book(Item):
    def __init__(self, item_id, title, year, author, isbn):
        super().__init__(item_id, title, year)
        self.author = author
        self.isbn = isbn
        self.status = 'доступна'

    def __str__(self):
        return f"Книга '{self.title}' ({self.year}) Автор: {self.author}, ISBN: {self.isbn}, Статус: {self.status}"


class Reader:
    def __init__(self, reader_id, name):
        self.reader_id = reader_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        borrowed_titles = ', '.join([book.title for book in self.borrowed_books])
        return f'Читатель {self.name}(ID:{self.reader_id}), Книги: {borrowed_titles}'


class Library:
    def __init__(self):
        self.books = {}
        self.readers = {}

    # Добавление книги в библиотеку
    def add_book(self, book):
        if book.item_id not in self.books:
            self.books[book.item_id] = book
        else:
            raise Exception("Книга с таким ID уже существует")

    # Регистрация нового читателя
    def register_reader(self, reader):
        if reader.reader_id not in self.readers:
            self.readers[reader.reader_id] = reader
        else:
            raise Exception("Читатель с таким ID уже зарегистрирован")

    # Выдача книги читателю
    def lend_book(self, book_id, reader_id):
        if book_id not in self.books:
            raise Exception("Книга не найдена")

        book = self.books[book_id]
        if book.status != 'доступна':
            raise Exception("Книга уже выдана")

        if reader_id not in self.readers:
            raise Exception("Читатель не зарегистрирован")

        reader = self.readers[reader_id]
        reader.borrowed_books.append(book)
        book.status = 'выдана'

    # Возврат книги читателем
    def return_book(self, book_id, reader_id):
        if book_id not in self.books or reader_id not in self.readers:
            raise Exception("Книга или читатель не найдены")

        book = self.books[book_id]
        reader = self.readers[reader_id]

        if book not in reader.borrowed_books:
            raise Exception("Эта книга не была взята данным читателем")

        reader.borrowed_books.remove(book)
        book.status = 'доступна'

    # Поиск всех книг определенного автора
    def find_books_by_author(self, author):
        return [book for book in self.books.values() if book.author.lower() == author.lower()]

    # Получение списка книг текущего читателя
    def get_reader_books(self, reader_id):
        if reader_id not in self.readers:
            raise Exception("Читатель не найден")

        reader = self.readers[reader_id]
        return reader.borrowed_books


# Пример использования библиотеки
if __name__ == "__main__":
    library = Library()

    # Создание книги
    book1 = Book(1, "Война и мир", 1869, "Л.Н. Толстой", "978-5-17-982347-1")

    # Регистрация читателя
    reader1 = Reader(1, "Иван Иванов")

    # Добавляем книгу в библиотеку
    library.add_book(book1)

    # Регистрируем читателя
    library.register_reader(reader1)

    try:
        # Выдаем книгу читателю
        library.lend_book(1, 1)

        # Проверяем выданные книги читателя
        print("\nВыданные книги:")
        for book in library.get_reader_books(1):
            print(book)

        # Возвращаем книгу обратно
        library.return_book(1, 1)

        # Ищем книги по автору
        found_books = library.find_books_by_author("Л.Н. Толстой")
        print("\nНайденные книги по автору:")
        for book in found_books:
            print(book)

    except Exception as e:
        print(f"Произошла ошибка: {e}")