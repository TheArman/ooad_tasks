class Book:
    # __slots__ = 'book_title', 'author'

    def __init__(self, book_title: str, author: str) -> None:
        self.book_title = book_title
        self.author = author

    def __str__(self):
        return f'{self.author}: {self.book_title}'

    def __repr__(self):
        return self.__str__()


class Library:
    def __init__(self):
        self.list_of_books = []

    def add_books(self, book: Book) -> None:
        self.list_of_books.append(book)

    def library_details(self) -> list:
        return self.list_of_books


book_1 = Book('OOAD', 'Grady Booch')
book_2 = Book('Fluent Python', 'Luciano Ramalho')
book_3 = Book('Effective Python', 'Brett Slatkin')
book_4 = Book('Learning Python', 'Mark Lutz')

library = Library()

library.add_books(book_1)
library.add_books(book_2)
library.add_books(book_3)
library.add_books(book_4)

print(library.library_details())
