import json
import pickle


class Car:
    def __init__(self, label, year, manufacturer, engine, color, price):
        self.__label = label
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine = engine
        self.__color = color
        self.__price = price

    def get_label(self):
        return self.__label

    def set_label(self, value):
        self.__label = value

    def get_year(self):
        return self.__year

    def set_year(self, value):
        self.__year = value

    def get_manufacturer(self):
        return self.__manufacturer

    def set_manufacturer(self, value):
        self.__manufacturer = value

    def get_engine(self):
        return self.__engine

    def set_engine(self, value):
        self.__engine = value

    def get_color(self):
        return self.__color

    def set_color(self, value):
        self.__color = value

    def get_price(self):
        return self.__price

    def set_price(self, value):
        self.__price = value


car = Car('BMW', "1998", 'Germany', '8v', 'red', '1 million $')
print(car.__dict__)
with open('car_js.json', 'w') as f:
    json.dump(car.__dict__, f)

with open('car_js.json', 'r') as f:
    sr = json.load(f)
print(sr)

with open('file_car_pickle.txt', 'wb') as f:
    pickle.dump(car.__dict__, f)

with open('file_car_pickle.txt', 'rb') as f:
    deserialize = pickle.load(f)
print(deserialize)
