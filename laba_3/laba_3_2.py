##2)Напишите классы «Книга» (с обязательными полями: название, автор,
#код), «Библиотека» (с обязательными полями: адрес, номер) и
#корректно свяжите их. Код книги должен назначаться автоматически
#при добавлении книги в библиотеку (используйте для этого
#статический член класса). Если в конструкторе книги указывается в
#параметре пустое название, необходимо сгенерировать исключение
#(например, ValueError). Книга должна реализовывать интерфейс
#Taggable с методом tag(), который создает на основе строки набор тегов
#(разбивает строку на слова и возвращает только те, которые
#начинаются с большой буквы). Например, tag() для книги с названием
#‘War and Peace’ вернет список тегов [‘War’, ‘Peace’].
#Реализуйте классы таким образом, чтобы корректно выполнялся следующий код:
#lib = Library(1, ’51 Some str., NY’)
#lib += Book(‘Leo Tolstoi’, ‘War and Peace’)
#lib += Book(‘Charles Dickens’, ‘David Copperfield’)
#for book in lib:
# вывод в виде: [1] L.Tolstoi ‘War and Peace’
#print(book)
# вывод в виде: [‘War’, ‘Peace’]
#print(book.tag())

from abc import abstractmethod

class Taggable:
    @abstractmethod
    def tag(self):
        pass


class Book(Taggable):
    count = 0

    def __init__(self, author:str, name:str):
        if not isinstance(author,str):
            raise ValueError("Пустая строка",author = 0)
        if not isinstance(name,str):
            raise ValueError("Пустая строка", name = '0')
        Book.count += 1
        self._name = name
        self._author = author
        self._code = Book.count

    def tag(self):
        words = self._name.split()
        return [word for word in words if word.istitle()]

    def __str__(self):
        return "[%d] %s '%s'" % (self._code, self._author, self._name)


class Library(object):

    def __init__(self, number:int, adress:str):
        if not isinstance(number,int):
            raise ValueError("Пустая строка",adress = 0)
        if not isinstance(adress,str):
            raise ValueError("Пустая строка", number = '0')

        self._adress = adress
        self._number = number
        self._books = []

    def __add__(self, book):
        self._books += [book]
        return self

    def __iadd__(self, book):
        return self.__add__(book)

    def __iter__(self):
        for book in self._books:
            yield book


lib = Library(1,'51 Some str., NY')
lib += Book('Leo Tolstoi', 'War and Peace')
lib += Book('Charles Dickens', 'David Copperfield')
for book in lib:
    print(book)
    print(book.tag())