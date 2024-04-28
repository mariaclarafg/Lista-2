class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_data(self):
        print(f"Title: {self.title}\nAuthor: {self.author}")


class PhysicalBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def show_data(self):
        super().show_data()
        print(f"Pages: {self.pages}")

book1 = PhysicalBook("Daisy Jones and The Six", "Taylor J. Reid", 302)
book1.show_data()
