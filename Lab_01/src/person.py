class Person:
    def __init__(self, first_name, last_name, age = None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_adult(self):
        if self.age is None:
            raise ValueError("Ageisnotset")
        return self.age >= 18

    def celebrate_birthday(self):
        if self.age is None:
            raise ValueError("Ageisnotset")
        self.age += 1
        return self.age