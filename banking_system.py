class User:

    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password
        self.items = []

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class BankUser(User):

    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
        self.user = name

    # change You in these statements to the name of the actual user when depost, withdraw, or show_balance
    def show_balance(self):
        print(self.name, 'currently has a balance of: $' + str(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print(
                'You are currently exceeding your balance. Please reduce your withdrawal amount.')
            return

    def deposit(self, amount):
        self.balance += amount
        self.show_balance()

    def transfer_money(self, user, amount):
        if amount > self.balance:
            print('\nYou are exceeded your balance - please reduce transfer amount.')
            return

        print('\nYou are currently transferring: $' +
              str(amount), 'to the account of', user.name)
        print('Authentication required:')
        pinnumber = int(input('Enter your pin: '))

        if self.pin == pinnumber:
            print('Transfer Complete.')
            self.balance -= amount
            user.balance += amount
            self.show_balance()
            user.show_balance()
            return True
        else:
            print('Invalid PIN. Transfer Cancelled.')
            self.show_balance()
            user.show_balance()
            return False

    def request_money(self, user, amount):
        print('\n' + self.name, 'is currently requesting',
              amount, 'from', user.name)
        print('Authentication Required')
        pinnumber = int(
            input('Please enter the pin of the user you are requesting money from: '))

        if user.pin == pinnumber:
            print('Further authentication required')
            passwordinput = input(
                'Please enter your password: ')
            if passwordinput == self.password:
                self.balance += amount
                user.balance -= amount
                print(user.name, 'sent: $' + str(amount))
                self.show_balance()
                user.show_balance()
                return
            else:
                print('Invalid password. Money Request Cancelled.')
                self.show_balance()
                user.show_balance()
                return
        else:
            print('Invalid PIN - Money Request Cancelled.')
            self.show_balance()
            user.show_balance()
            return


""" Driver Code for Task 1"""
# user = User('Bob', 1234, 'password')
# print(user.name, user.pin, user.password)

"""Driver Code for Task 2"""
'''user = User('Liam', 1234, 'password')
print(user.name, user.pin, user.password)
user.change_name('Yasser')
user.change_pin(4321)
user.change_password('newpassword')
print(user.name, user.pin, user.password)'''

"""Driver Code for Task 3"""
'''user = BankUser('Liam', 1234, 'password')
print(user.name, user.pin, user.password, user.balance)'''

"""Driver Code for Task 4"""
'''user = BankUser('Liam', 1234, 'password')
print(user.name, user.pin, user.password, user.balance)
user.show_balance()
user.deposit(1000)
user.show_balance()
user.withdraw(888)
user.show_balance()'''

"""Driver Code for Task 5"""
'''user1 = BankUser('Liam', 1234, 'password')
user2 = BankUser('Yasser', 4321, 'password1')
user2.deposit(5000)
user1.show_balance()
user2.transfer_money(user1, 500)
user2.request_money(user1, 250)'''
