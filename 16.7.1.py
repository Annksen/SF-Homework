class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


baron = Cat(name="Baron", gender="m", age="2")
sam = Cat(name="Sam", gender="m", age="2")

cats = {baron, sam}

for cat in cats:
    print(cat.name, cat.gender, cat.age)