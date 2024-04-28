class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_data(self):
        print(f"Title: {self.title}\nAuthor: {self.author}")

class LibraryBook(Book):
    def __init__(self, title, author, code):
        super().__init__(title, author)
        self.code = code

    def show_data(self):
        super().show_data()
        print(f"Code: {self.code}")

library_book = LibraryBook("Felicidade Clandestina", "Clarice Lispector", "FCCL900")
library_book.show_data()
