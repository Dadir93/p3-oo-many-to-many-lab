class Book:
    members = []

    def __init__(self, title):
        self.title = title
        self.__class__.members.append(self)

    def contracts(self):
        return [contract for contract in Contract.members if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Author:
    members = []

    def __init__(self, name):
        self.name = name
        self.__class__.members.append(self)

    def contracts(self):
        return [contract for contract in Contract.members if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book object.")
        if not isinstance(date, str):
            raise Exception("Invalid date format.")
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties format.")

        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Contract:
    members = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author object.")
        if not isinstance(book, Book):
            raise Exception("Invalid book object.")
        if not isinstance(date, str):
            raise Exception("Invalid date format.")
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties format.")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.members.append(self)