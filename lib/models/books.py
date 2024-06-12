class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_lent = False
        self.lent_to = None

    def __str__(self):
        return f"'{self.title}' by {self.author}"


