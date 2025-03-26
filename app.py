import json

class student_mode:
    def __init__(self, name, classes, work):
        self.name = name
        self.classes = classes
        self.work = work
    def display_info(self):
        return f"Student: {self.name}, Classes: {self.classes}, Work: {self.work}"
