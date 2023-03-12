# class Rectangle:
#     def __init__(self, x, y, w, h):
#         self.x = x
#         self.y = y
#         self.w = w
#         self.h = h
#
#     def __str__(self):
#         return 'Rectangle: {}, {}, {}, {}'.format(self.x, self.y, self.w, self.h)
#
# r = Rectangle(5, 10, 50, 100)
# print(r)

# #
# class Client:
#     def __init__(self, name, surname, city, balance):
#         self.name = name
#         self.surname = surname
#         self.city = city
#         self.balance = balance
#
# ivan = Client(name='Иван ', surname='Петров.', city='Москва.', balance='Баланс: 50 руб')
# print(ivan.name, ivan.surname, ivan.city, ivan.balance)

class Guests:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'''{self.name}{self.surname}".{self.city}.Баланс: {self.balance}руб.'''
    def get_guest(self):
        return f'{self.name}{self.surname},г.{self.city}'

g1 = Guests('Иван', 'Петров', 'Москва', '50')
g2 = Guests('Екатерина', 'Иванова', 'Самара', '200')
g3 = Guests('Елена', 'Николаева', 'Тверь', '550')

guest_list = [g1, g2, g3]

for guest in guest_list:
    print(guest.get_guest())