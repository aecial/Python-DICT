class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display1(self):
        print('Username: ', self.username, 'Password:', self.password)

# Establish Inheritance
class Admin(User):
    # Override Init Method
    def __init__(self, username, password, code):
        self.username = username
        self.password = password
        self.code = code
        # access init in super class
        super().__init__(username, password)

    def display2(self):
        print('SUB Username: ', self.username, 'Password:', self.password, 'Code: ', self.code)
        
    def display3(self):
        # super method allows to call a method from the base class
        super().display1()
        print('display3 to')

a_1 = Admin('ted', 'pass1234', '1234')
u_1 = User('kled', 'pass1234')

a_1.display3()
u_1.display1()