class Book:

    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    @staticmethod
    def edition():
        y = int(input('Year of edition. Has to be 1894 or 1998: '))
        if y == book1.year:
            return 'Conan Doyle'
        elif y == book2.year:
            return 'Stephen King'
        else:
            return print('You made mistake!'), Book.edition()

    @staticmethod
    def description():
        if Book.edition() == 'Conan Doyle':
            print(
                str(f'This book {book1.title}  of {book1.genre} genre were written by {book1.author} in {book1.year}.'))
            print(repr(
                f'This book {book1.title}  of {book1.genre} genre were written by {book1.author} in {book1.year}.'))

        else:
            print(repr(
                f'This book {book2.title}  of {book2.genre} genre were written by {book2.author} in {book2.year}.'))
            print(
                str(f'This book {book2.title}  of {book2.genre} genre were written by {book2.author} in {book2.year}.'))


book1 = Book(author='Conan Doyle', title='THE MEMOIRS OF SHERLOCK HOLMES', year=1894, genre='detective')
book2 = Book(author='Stephen King', title="BAG OF BONES", year=1998, genre='fantasy')

Book.description()
