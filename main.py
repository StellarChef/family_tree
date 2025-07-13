import json
from src.person import Person
from src.personmanager import PersonManager

def main():
    print("If you want to Add new Person please write Add")
    print("If you want to show people please write show")
    print("To exit the program write exit")

    while True:
        choice = input("Choose: ").lower()

        if choice == "add":
            PersonManager.addPerson()
        elif choice == "show":
            PersonManager.showPeople()
        elif choice == "exit":
            break
        else:
            print("Incorrect data")

    

if __name__ == "__main__":
    main()


	
