# Class - A blueprint for creating objects 

class Car:
    def __init__(self, __make, model):
        self.__make = __make # dot notation - <object>.<attr/method>
        self.model = model
       # self.__make = __make # __make on all instances of __make>results in AttributeError, makes the attr private

    def start(self):
        print(f'{self.__make} {self.model} Car started!')

    def display(self):
        return(f'This is a {self.__make} {self.model}')

    def __str__(self): # Returns a string representation of the object
        return(f'This is a {self.__make} {self.model}')

# Getter
    def get_make(self):
        return self.__make # Authorize # if condition
    # Side-effects
    
# Setter
    def set_make(self, new_make):
        self.__make = new_make # Validate new_make > # Authorize

class PetrolCar(Car):
        def __init__(self, make, model, tank_capacity_l):
            super().__init__(make, model)
            self.tank_capacity_l = tank_capacity_l

# Main
my_car = PetrolCar('Mercedes', 'Gclass', 100)

# my_car = Car('Toyota', 'Camry')
your_car = Car('Hyundai', 'Accent')


# my_car is now an object of class 'Car'

# print(my_car)
print(your_car)
# print(my_car.__dict__)
# print(your_car.__dict__)

# my_car.start()
your_car.start()
# print(my_car.get_make())
print(my_car.display())
# print(my_car)










# Encapsulation bank acc
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance  # Private attribute (Encapsulated)

#     # Getter method to read private data safely
#     def get_balance(self):
#         return self.__balance

#     # Setter method to modify private data with validation
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited ${amount}. New balance: ${self.__balance}")
#         else:
#             print("Invalid deposit amount!")

# # Usage
# account = BankAccount("Alice", 1000)
# account.deposit(500)
# # print(account.__balance)  # Throws an AttributeError (Protected)
# print(f"Balance via getter: ${account.get_balance()}")



