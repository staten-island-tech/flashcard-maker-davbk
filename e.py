import json

streak = 0
points = 0

class Teacher:
    def __init__(self):
        self.aa = {}

    def makekey(self):
        key = input("Enter a question: ")
        value = input("Enter the answer: ")
        self.aa[key] = value
        print(self.aa)

    def save(self):
        with open("Flashcards.json", 'w') as file:
            json.dump(self.aa, file, indent=4)
        print("saved")

class Student:
    def __init__(self, flashcards):
        self.flashcards = flashcards

    def start(self):
        global streak, points
        for question, answer in self.flashcards.items():
            user_input = input(f"{question}? ")
            if user_input.lower() == answer.lower():
                streak += 1
                points += 1
                print("correct")
            else:
                streak = 0
                print(f"wrong")
        print(f"points: {points}, streak: {streak}")
user_input = input("Choose a class (student/teacher/exit): ").lower()
if user_input == "teacher":
    t = Teacher()
    while True:
        t.makekey()
        e = input("add another? ")
        if e == "no":
            break
    t.save()
elif user_input == "student":
    try:
        with open("Flashcards.json", 'r') as file:
            data = json.load(file)
        s = Student(data)
        s.start()
    except FileNotFoundError:
        print("No flashcards found. A teacher needs to create them first.")
else:
    print("Exiting...")
