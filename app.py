import json

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def to_dict(self):
        return {"question": self.question, "answer": self.answer}
    def teacher():
        flashcards = []
        while True:
            question = input ("Enter a question: ")
            if question == "quit":
                break
            answer = input("Enter answer: ")
            flashcard = Flashcard(question, answer)
            flashcards.append(flashcard)

