import json

streak = 0
points = 0

class Teacher:
    def __init__(self):
        self.flashcards = {}

    def make_flashcards(self):
        key = input("Enter a term: ")
        value = input("Enter the definition: ")
        self.flashcards[key] = value
        print(self.flashcards)

    def save_flashcards(self):
        with open("Flashcards.json", "w") as f:
            json.dump(self.flashcards, f, indent=4)


class Student:
    def __init__(self):
        with open("Flashcards.json", "r") as f:
            self.flashcards = json.load(f)

    def quiz(self):
        global streak
        global points
        for key, value in self.flashcards.items():
            answer = input(f"What is the definition of '{key}'? ")
            if answer == value:
                print("correct")
                streak += 1
                points += 1
            else:
                print(f"wrong")
                streak = 0
            print(f"Streak: {streak}")
            print(f"Points: {points}")

def main():
    while True:
        user_input = input("Choose a class (student/teacher/exit): ").strip().lower()

        if user_input == "student":
            s = Student()
            s.quiz()
        elif user_input == "teacher":
            t = Teacher()
            t.make_flashcards()
            t.save_flashcards()
        elif user_input == "exit":
            print("Exiting program.")
            break
        else:
            exit
main()

