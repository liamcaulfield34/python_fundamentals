class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password):
        self.password = password
        print('Your pasword has been changed to', self.password)


user1 = User("jane", "jane@nucamp.co", "janespassword")
print(user1.password)
user1.change_password('ballsack')


class BankUser(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0

    def check_balance(self):
        print(self.name, 'your current balance is', self.balance)


user3 = BankUser('Liam', 'laim@gmail.com', 'liams')
user3.check_balance()
