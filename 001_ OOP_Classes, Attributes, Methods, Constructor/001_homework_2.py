class Book:

    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre


class Resume:

    resumeCD = """          “The Memoirs of Sherlock Holmes” was initially published in 1894 after each of 
    the individual stories contained within had appeared separately in The Strand magazine. This collection
    was the follow-up to “The Adventures of Sherlock Holmes” which introduced the detective
    and his loyal companion Dr. John Watson. The Memoirs are generally considered the superior
    to the collection which introduced the detective, but not as strong as the stories he solved
    in the next collection following his resurrection. The Memoirs of Sherlock Holmes
    draws to a close with Dr. John Watson disconsolate in his conviction that Holmes and
    his nemesis Prof. Moriarty fell to their deaths after a struggle atop Reichenbach Falls."""

    resumeSK = """          “Bag of Bones” is a 1998 fantasy novel by American author Stephen King.
    Set in the fictional unincorporated town of TR-90, Maine, it follows an author,
    Mike Noonan, who suffers from writer’s block. Having isolated himself at his lake house to write,
    Noonan begins to experience delusions linked to the untimely death of his wife four years earlier.
    The plot borrows some of its tensions, events, and characterizations from Rebecca,
    a Gothic novel by English author Daphne du Maurier. Though not his most famous work,
    Bag of Bones is considered one of King’s best written and has been the recipient of many awards,
    including the British Fantasy Award for Best Novel and the Bram Stoker Award."""


book1 = Book(author='Conan Doyle', title='THE MEMOIRS OF SHERLOCK HOLMES', year=1894, genre='detective')
book2 = Book(author='Stephen King', title="BAG OF BONES", year=1998, genre='fantasy')

print(f'This book {book1.title}  of {book1.genre} genre were written by {book1.author} in {book1.year}.',
      Resume.resumeCD, sep='\n\n')

print('****************************************')

print(f'This book {book2.title}  of {book2.genre} genre were written by {book2.author} in {book2.year}.',
      Resume.resumeSK, sep='\n\n')
