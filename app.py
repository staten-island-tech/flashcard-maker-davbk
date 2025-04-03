import json

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"
class Student(User):
    def __init__(self, question, answer, streak): 
        super().__init__(question, answer)
        self.streak = streak
