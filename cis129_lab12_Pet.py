# Lab 12 Pet class
# Luis Camacho
# May 17, 2025
# Creates Pet class and myPet object based on user  
# input then returns values stored in myPet object




def main():
    # Creates pet object
    myPet = Pet()

    # Sets value for name
    myPet.set_name(input('Enter a pet name:'))

    # Sets value for type
    myPet.set_type(input('Enter a pet type:'))

    # Sets value for age
    myPet.set_age(input('Enter a pet age:'))

    # Prints name
    print('The pet name is',myPet.get_name())

    # Prints type
    print('The pet type is',myPet.get_type())

    # Prints age
    print('The pet age is',myPet.get_age())



# Defines Pet class
class Pet:
    def __init__(self, name, type, age):
        self.name = ''
        self.type = ''
        self.age = ''

    # Defines name
    def set_name(self, name):
        self.name = name
    
    # Defines type
    def set_type(self, type):
        self.type = type

    # Defines age
    def set_age(self, age):
        self.age = age

    # Returns name
    def get_name(self):
        return(self.name)
    
    # Returns type
    def get_type(self):
        return(self.type)
    
    # Returns age
    def get_age(self):
        return(self.age)
    
main()
