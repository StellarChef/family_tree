class Person:
    def __init__(self, name, surname, dateOfBirth, dateOfDeath,):
        self.name = name
        self.surname = surname
        self.dateofBirth = dateOfBirth
        self.dateOfDeath = dateOfDeath
        
        self.children = []
        self.parents = []
        self.spose = None