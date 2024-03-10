class Customers:
    greeting = 'Welcome to Coffee Place!'
    def __init__(self, name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total

c_1 = Customers('Elaine', 'Strawberry Fapuccino', 'Tuna Wrap', 270)
c_2 = Customers('Jerry', 'Caramel Macchiato', 'Glazed Donut', 230)

print(Customers.greeting)

print(c_1.name)
print(c_1.food)
print(c_1.beverage)
print(c_1.total)
print('-------------')
print(c_2.name)
print(c_2.food)
print(c_2.beverage)
print(c_2.total)