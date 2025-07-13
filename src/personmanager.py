from src.person import Person

class PersonManager:
    people = []

    @staticmethod
    def addPerson():
        print("\n----- Adding a person --------")
        name = input("First name: ")
        surname = input("Last name: ")
        dateofBirth = input("Date of birth: ")
        dateOfDeath = input("Date of death (leave blank if still alive): ")

        if dateOfDeath.strip() == "":
            dateOfDeath = None

        newperson = Person(name, surname, dateofBirth, dateOfDeath)
        PersonManager.people.append(newperson)

        print(f"Person added: {name} {surname}")

    @staticmethod
    def showPeople():
        print("------------ People list -----------")
        if not PersonManager.people:
            print("No people in memory.")
        else:
            for person in PersonManager.people:
                print(f"{person.name} {person.surname} | Born: {person.dateofBirth} | "
                      f"Died: {person.dateOfDeath if person.dateOfDeath else 'Alive'}")