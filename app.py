class student:
    def __init__ (self, name, classes):
        self.name = name
        self.classes = classes
    def work(self, assignments):
        self.classes.remove(assignments)
        print(self.classes)
david = student("David", ['Geometry Delta Math', 'Chemistry Homework', 'APWH Project'])
david.work('Chemistry Homework')