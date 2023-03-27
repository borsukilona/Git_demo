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


