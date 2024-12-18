class Author:
    all = []

    def __repr__(self):
        return f"<Author name: {self.name}>"
    
    def __init__(self,name):
        self.name = name
        self.__class__.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self,book,date,royalties):
        return Contract(self,book,date,royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
    
    
class Book:
    all = []

    def __repr__(self):
        return f"<Book title: {self.title}>"
    
    def __init__(self,title):
        self.title = title
        self.__class__.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]
    

class Contract:

    @classmethod
    def contracts_by_date(cls,date):
        return [contract for contract in cls.all if contract.date == date]
    
    all = []

    def __repr__(self):
        return f"<Contract author: {self.author.name}, book: {self.book.title}, date: {self.date}, royalites: {self._royalties}>"

    def __init__(self,author,book,date,royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self,value):
        if isinstance(value,Author):
            self._author = value
        else:
            raise Exception

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self,value):
        if isinstance(value,Book):
            self._book = value
        else:
            raise Exception
        
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self,value):
        if isinstance(value,str):
            self._date = value
        else:
            raise Exception
    
    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self,value):
        if isinstance(value,int):
            self._royalties = value
        else:
            raise Exception
    