class Man():
    """Create a new man"""

    def __init__(self, name, age, height, weight):
        """Initialization of the person's attributes - name, age, height, weight"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.sex = "male" #аттрибут пола по умолчанию будет иметь мужской пол
        print("Person is created")

    def description_person(self):
        """Get description of the created man"""
        description = f"{self.name} has age {self.age} and is {self.height} height and weights {self.weight} kg"
        print(description)

    def get_weight(self):
        """Get weight of the created man"""
        print(f"Weight of the {self.name} is {self.weight} kg")

    def get_sex(self):
        """Get sex of the created man"""
        print(f"Sex of the {self.name} is {self.sex}")

    def update_sex(self, sx):
        """Change the default 'male' sex to the needed one"""
        self.sex = sx


# ----------------------------------------------------------Наследник---
class Warrior(Man):
    """Create class of warrior, which is an inheritor of class Man"""

    def __init__(self, name, age, height, weight):
        """Initialization of the warrior's attributes - name, age, height"""
        """
        Показываем, что наш класс наследует от класса Men (super-class) атрибуты (обязательно ВСЕ обязательные аттрибуты родителя)
        super() связывает __init__ потомка с методом  __init__ родителя (супер-класса)
        Если у родительского аттрибута будет дефолтное значение, то это дефолтное значение будет и у потомка
        Так же мы можем переопределить значение аттрибута у потомка
        """
        super().__init__(name, age, height, weight)
        self.rage = 100 # ярость! (у война должна быть ярость!)

    # методы потомков доступны только для потомков
    def get_rage(self):
        """Get rage of the created warrior"""
        print(f"Rage of the warrior {self.name} is {self.rage}!")

    def update_rage(self, rg):
        """Change the default '100' rage to the needed one"""
        self.rage = rg

    # переопределение метода родителя
    def description_person(self):
        """Refactor parent's description method"""
        description = f"{self.name} has age {self.age} and is {self.height} and has {self.rage} of rage!"
        # print(description)
        return description


# ----------------------------------------------------------Родитель---
man = Man("Sergey", 35, 175, 85)
man.description_person()
# Sergey has age 35 and is 175 height and weights 85 kg
man.get_weight()
# Weight of the Sergey is 85 kg
man.get_sex()
# Sex of the Sergey is male

woman = Man("Ilona", 25, 156, 45)
'''
woman.sex = "female" # изменили дефолтный male на нужный female
woman.get_sex()
# Sex of the Ilona is female
'''
woman.update_sex("female")
woman.get_sex()
# Sex of the Ilona is female

# ----------------------------------------------------------Наследник---
warrior = Warrior("Conon", 32, 200, 100)

# используем метод родителя для потомка:
warrior.description_person()
# Conon has age 32 and is 200 height and weights 100 kg
warrior.get_sex()
# Sex of the Conon is male
warrior.update_sex("unknown")
warrior.get_sex()
# Sex of the Conon is unknown

# используем метод потомка для потомка:
warrior.get_rage()
# Rage of the warrior Conon is 100!
warrior.update_rage(500)
warrior.get_rage()
# Rage of the warrior Conon is 500!
print(warrior.description_person())
# Conon has age 32 and is 200 and has 500 of rage!
