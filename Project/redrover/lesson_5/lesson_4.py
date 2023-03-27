class Dog:
    def __init__(self, name, breed, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.__breed = breed

    def get_breed(self):
        print(self.__breed)
        return self.__breed

    def set_breed(self, breed):
        self.__breed = breed

    def tell_about(self):
        print(f'My name is {self.name},'
              f'\ni am {self.age} years old'
              f'\nand have {self.color} color,'
              f'\nmy breed is {self.get_breed()}')


class Doggy(Dog):

    def __init__(self, name, breed, age, color):
        super().__init__(name, breed, age, color)

    def sit_down(self):
        print('I can sit down!')

    def bark(self):
        print('I can bark load!')


dog1 = Dog('Lola', 'chau-chau', 3, 'grey')
dog1.get_breed()  # 'chau-chau'
dog1.set_breed('taksa')
dog1.get_breed()  # taksa
dog1.tell_about()
# My name is Lola,
# i am 3 years old
# and have grey color,
# my breed is taksa

dog2 = Doggy('Doggy', 'ovchar', 5, 'black')
dog2.tell_about()
# My name is Doggy,
# i am 5 years old
# and have black color,
# my breed is ovchar
dog2.get_breed()  # ovchar
dog2.set_breed('sharpey')
dog2.get_breed()  # sharpey
dog2.tell_about()
# My name is Doggy,
# i am 5 years old
# and have black color,
# my breed is sharpey
dog2.sit_down()  # I can sit down!
dog2.bark()  # I can bark load!