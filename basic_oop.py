# Class - A blueprint for creating objects 

class Car:
    def __init__(self, __make, model, engine):
        self.__make = __make # dot notation - <object>.<attr/method>
        self.model = model
        self.engine = engine
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

# Inheritance - 'is-a' relationship
class PetrolCar(Car):
        def __init__(self, make, model, engine, tank_capacity_l):
            super().__init__(make, model, engine)
            self.tank_capacity_l = tank_capacity_l


        def __str__(self):
            return(f'{super().__str__()}. It has a {self.tank_capacity_l}l tank.')

# class ElectricCar(Car):
#     def __init__(self, make, model, battery_capacity_kwh):
#         super().__init__(make, model)
#         self.battery_capacity_kwh = battery_capacity_kwh

#     def __str__(self):
#         return (f'{super().__str__()}. It has a {self.battery_capacity_kwh}Kwh battery')

# Composition - 'has-a' relationship
class Engine:
    def __init__(self, type, max_power_kw):
        self.type = type
        self.max_power_kw = max_power_kw

    def __str__(self):
        return(f'This is a {self.type} engine with a maximum power of {self.max_power_kw}KW')



# Main

engine1 = Engine(type='petrol', max_power_kw=235)


my_car = PetrolCar(make='Mercedes', model='GWagon', tank_capacity_l=100, engine=engine1)
print(my_car)
print(my_car.engine)
print(my_car.model)

# my_car = Car('Toyota', 'Camry')
# your_car = Car('Hyundai', 'Accent')
# print(your_car)

# other_car = ElectricCar('Kia', 'EV3', 81.4)
# print(other_car)



# my_car is now an object of class 'Car'



# print(my_car.__dict__)
# print(your_car.__dict__)

# my_car.start()
# your_car.start()
# print(my_car.get_make())
# print(my_car.display())
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



