# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: double-underscore properties are hidden from other 
    __booklist = None


    # TODO: create a class method
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES
    # In Python, the @classmethod decorator is used to define a class method. 
    # A class method is a method that is bound to the class and not the instance of the class. 
    # It takes the class itself as its first parameter, conventionally named cls.

    # TODO: create a static method
    # Static methods don't modify the state of either the class or instance.
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist
    

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    # Below examples of instance methods. They take (self, ) as the first parameter 
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title

        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f'{booktype} is not a valid book type')
        else:
            self.booktype = booktype


# TODO: access the class attribute
print('Book types: ', Book.get_book_types())


# TODO: Create some book instances
b1 = Book('Title1', 'HARDCOVER')
b2 = Book('Title2', 'PAPERBACK')


# TODO: Use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)