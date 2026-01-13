class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def write(self, text):
        if self.file is not None and not self.file.closed:
            self.file.write(text)
        else:
            raise ValueError("Файл закрыт или не открыт.")

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file is not None:
            self.file.close()

# Пример использования
# with FileManager('example.txt') as manager:
#     manager.write('Привет, мир!\nЭто тестовая строка.')