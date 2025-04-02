import json

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"
class Student(User):
    def __init__(self, name, email, student_id): 
        self.student_id = student_id
class Teacher(User):
    def __init__(self, name, email, teacher_id):
        self.teacher_id = teacher_id