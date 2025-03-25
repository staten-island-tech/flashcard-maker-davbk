import json

class student:
    def __init__(self, name, classes, work):
        self.name = name
        self.classes = classes
        self.work = work
    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"


