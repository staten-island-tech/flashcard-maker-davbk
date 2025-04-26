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

    def save_flashcards(self):
        with open("Flashcards.json", "w") as f:
            json.dump(self.flashcards, f)

class Student:
    def __init__(self):
        with open("Flashcards.json", "r") as f:
            self.flashcards = json.load(f)

    def quiz(self):
        global streak
        global points
        for key in self.flashcards:
            answer = input(f"What is the definition of '{key}'? ")
            if answer == self.flashcards[key]:
                print("correct")
                streak += 1
                points += 1
            else:
                print(f"wrong")
                streak = 0
            print(f"Streak: {streak}")
            print(f"Points: {points}")

mode = input("teacher or student? ")

if mode == "teacher":
    t = Teacher()
    t.make_flashcards()
    t.save_flashcards()

elif mode == "student":
    s = Student()
    s.quiz()

else:
    exit
