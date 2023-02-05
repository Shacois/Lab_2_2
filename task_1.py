


books = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    def __init__(self, id: int, name: str, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages
        if not isinstance(id, int):
            raise TypeError("Количество страниц должно быть типа int")
        if id <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return f'Книга "{self.name}"'
    def __repr__(self) -> str:
        return f'Book(id = {self.id}, name = {self.name!r}, pages = {self.pages})'

class Library:
    def __init__(self, books = None):
        self.books = books
        if self.books is None:
            self.books = []

    def get_next_book_id(self):
        if self.books == []:
            return 1
        else:
            return len(books) + 1

    def get_index_by_book_id(self, index: int):
        for id, book in enumerate(self.books):
            if book.id == index:
                return index
        if index >= len(self.books):
            raise ValueError("Книги с запрашиваемым id не существует")



