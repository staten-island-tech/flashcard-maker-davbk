streak = 0
points = 0
import json

class Teacher:
    def __init__(self):
        self.aa = {}

    def makekey(self):
        key = input("enter a key: ")
        value = input("enter a value:")
        self.aa[key] = value
        print(self.aa)

    def save(self):
        with open("Flashcards.json", 'w') as file:
            json.dump(self.aa, file, indent=4)

w = Teacher()
w.makekey()
w.save()
class Flashcards:
    def __init__(self, answers, questions):
        self.answers = answers
        self.questions = questions
class Student:
    def __init__(self, teach_instance):
        global streak
        global points
        self.teach_instance = teach_instance
    def start(self):
        global streak
        global points
        answer = input("enter answer:")
        if answer == answer:
            streak += 1
            points += 1


"""     def to_dict(self):
        return {"question": self.question, "answer": self.answer}
    def teacher():
        flashcards = {}
        while True:
            question = input ("Enter a question: ")
            if question == "quit":
                break
            answer = input("Enter answer: ")
            flashcard = Flashcard(question, answer)
            flashcards.append(flashcard) """