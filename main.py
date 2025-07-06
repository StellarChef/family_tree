from curses.ascii import islower


class Person:
    def __init__(self, name, surname, dateOfBirth, dateOfDie):
        self.name = name
        self.surname = surname
        self.dateofBirth = dateOfBirth
        self.dateOfDie = dateOfDie

    def przedstaw_sie(self):
        print(f"Cześć! Jestem {self.name} {self.surname}")

class PersonMenago:
    person = []

    def addPerson():
        while True:
            print("\n----- Dodawanie osoby --------")
            name = input("name: ")
            surname = input("surname: ")

            newperson = Person(name,surname)
            PersonMenago.persons.append(newperson)

            next = input("Do you want to add another person: write t/n")

            if next.lower() == "n":
                break
            else:
                continue



def main():
    persons = []

    while True:
        print("\n---- Dodawanie osoby --------")
        name = input("Podaj imię: ")
        surname = input("Podaj nazwisko: ")

        new_person = Person(name, surname)
        persons.append(new_person)

        new_person.przedstaw_sie()

        dalej = input("Dodać kolejną osobę? (t/n): ")

        if dalej.lower() == "n":
            break

if __name__ == "__main__":
    main()


	
