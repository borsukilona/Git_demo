class Person():
    """Person Model"""

    def __init__(self, name, age):
        """Initialization of the person's attributes - name, age"""
        self.name = name
        self.age = age
        print("Person is created")

    # self - ссылка на экземпляр класса
    # name, age - это параметры экземпляра класса Person (и self помогает на это понять когда мы что-то создадим)

    """What this person can do"""

    def sing(self):  # self - ссылка на наш класс и на его атрибуты name, age
        """Ask a person to sing"""
        print(self.name + " sings")

    def dance(self):
        """Ask a person to dance"""
        print(self.name + " dances")


# ------------------------------------------------------------------
 # создание экземпляр men класса Person
man = Person("Sergey", 35)
# Person is created

print(man.name)
# Sergey

print(man.age)
# 25

man.dance()
# Sergey dances

man.sing()
# Sergey sings
# ------------------------------------------------------------------
# создание экземпляр woman класса Person
woman = Person("Ilona", 25)
# Person is created

woman.dance()
# Ilona dances

