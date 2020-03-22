# from datetime import date
#
# class User:
#     def __init__(self, name, surname, phone):
#         self.name = name
#         self.surname = surname
#         self.phone = phone
#         self.marks = list()
#         self.reviews = list()
#         self.orders = list()
#     def make_order(self, goods):
#         new_order = Order(self, goods)
#         self.orders.append(new_order)
#     def make_review(self, good, descr):
#         new_reviev = Review(self, good, descr)
#         self.reviews.append(new_reviev)
#     def make_mark(self, good, mark):
#         new_mark = Mark(self, good, mark)
#         self.marks.append(new_mark)
#
#
# class Good:
#     def __init__(self, name, descr, price):
#         self.name = name
#         self.descr = descr
#         self.price = price
#         self.marks = list()
#         self.reviews = list()
#     def __str__(self):
#         return f'{self.name} ({self.descr})'
#
# class Mark:
#     def __init__(self, good, user, value):
#         self.good = good
#         self.user = user
#         self.value = value
#         good.marks.append(self)
#
# class Review:
#     def __init__(self, user, good, descr):
#         self.good = good
#         self.user = user
#         self.descr = descr
#         good.reviews.append(self)
#     def __str__(self):
#         return f'Review for {self.good.name}\n {self.descr}\n Author: {self.user.name}'
#
# class Order:
#     def __init__(self, user, goods):
#         self.user = user
#         self.goods = goods
#         self.date = date.today()
#         self.state = 'new'
#
# u = [User('Yehor', 'Levchenko', 101),
#      User('Sergey', 'Limanchuk', 102)]
#
# g = [Good('Карандаш', 'perfect', 10),
#      Good('Резинка', '', 5)]
#
# y = u[0]
# pencil = g[0]
# y.make_order([pencil])
# good = y.orders[0].goods[0]
# print(f'{y.name} buy {good}')
# print(f'{y.name} pay {good.price}')
#
# y.make_review(pencil, 'Nice!')
# print(pencil.reviews[0])

# NewType = type("NewType", (object,), {"x": "hello"})
# n = NewType()
# print(n.x)
#
# import webbrowser
# webbrowser.open_new_tab('http://habrahabr.ru/') # Вернет True и откроет вкладку