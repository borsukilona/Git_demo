from base_person import Man


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

