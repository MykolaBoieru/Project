import questionary
from db import get_db, get_table_of_habits
from habit import Habit
from analyse import calculate_count, list_habits


def cli():
    i = True

    db = get_db()

    while i:

        choice = questionary.select(
            "What do you want to do?",
            choices=["Create", "Complete", "Analyse", "Delete", "List of habits", "Get help", "Exit"]).ask()

        if choice == "Create":
            name = questionary.text("What the name of your counter?").ask()

            desc = questionary.text("What's the description of your counter?").ask()
            category = questionary.select("Choose category of your habit?",
                                          choices=["sport", "study", "hobby"]).ask()
            frequency = int(questionary.select("Choose frequency of your habit in days",
                                               choices=["1", "7"]).ask())
            habit = Habit(name, desc)
            habit.category = category
            habit.frequency = frequency
            habit.store(db)

        elif choice == "Complete":
            try:
                name = questionary.select("Which habit do you want to complete?",
                                          choices=list_habits(db="main.db")).ask()

                habit = Habit(name, "no description")
                habit.increment()
                habit.add_event(db)
            except ValueError:
                print("You have to add a habit first!")

        elif choice == "Analyse":
            try:
                name = questionary.select("Which habit do you want to see?",
                                          choices=list_habits(db="main.db")).ask()
                count = calculate_count(db, name)
                print(f"{name} has been completed {count} times")
            except ValueError:
                print("You have to add a habit first!")

        elif choice == "Delete":
            try:

                name = questionary.select("Which habit do you want to delete?",
                                          choices=list_habits(db="main.db")).ask()
                habit = Habit(name, "no description")
                habit.delete(db, name)
            except ValueError:
                print("You have to add a habit first!")

        elif choice == "List of habits":
            print(get_table_of_habits(db))

        elif choice == "Get help":
            f = open("help.txt", "r")
            print(f.read())

        elif choice == "Exit":
            i = False
            print("Bye")
        else:
            pass


if __name__ == '__main__':
    cli()
