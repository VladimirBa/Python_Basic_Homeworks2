class Book:

    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def __repr__(self):
        return f'This book "{self.title}" of the {self.genre} genre were written by {self.author} in {self.year}.'

    def __str__(self):
        return f'This book "{self.title}" of the {self.genre} genre were written by {self.author} in {self.year}.'

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.genre != other.genre


book1 = Book(author='Conan Doyle', title='THE MEMOIRS OF SHERLOCK HOLMES', year=1894, genre='detective')
book2 = Book(author='Stephen King', title="BAG OF BONES", year=1998, genre='fantasy')

print(repr(book1))
print(book1)
print('*' * 10)
print(repr(book2))
print(book2)
print('*' * 10)
print('Were these books written in the same year?', book1 == book2)
print('*' * 10)
print('Are these books in different genres?', book1 != book2)
