import json
import pickle



class Book:
    def __init__(self, label, year, publisher, genre, author, price):
        self.__label = label
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def get_label(self):
        return self.__label

    def set_label(self, value):
        self.__label = value

    def get_year(self):
        return self.__year

    def set_year(self, value):
        self.__year = value

    def get_publisher(self):
        return self.__publisher

    def set_publisher(self, value):
        self.__publisher = value

    def get_genre(self):
        return self.__genre

    def set_genre(self, value):
        self.__genre = value

    def get_author(self):
        return self.__author

    def set_author(self, value):
        self.__author = value

    def get_price(self):
        return self.__price

    def set_price(self, value):
        self.__price = value


book = Book('Harry Potter', '1995', 'London news', 'Adventure', 'Joahn Rouling', '5$')

with open('file_book.txt', 'w') as f:
    json_str = json.dump(book.__dict__, f)

with open('file_book.txt', 'r') as f:
    sb = json.load(f)
print(sb)

with open('file_book_pickle.txt', 'wb') as f:
    pickle.dump(book.__dict__, f)

with open('file_book_pickle.txt', 'rb') as f:
    deserialize = pickle.load(f)
print(deserialize)
