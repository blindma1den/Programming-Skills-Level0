from models.Campus import Campus
from models.Student import Student


class Program:

    campuses: dict[str, Campus]
    name: str

    def __init__(self, name: str):
        self.campuses = {}
        self.name = name

    def add_campus(self, campus: Campus):
        self.campuses.update({campus.name: campus})

    def register_student(self):
        username = input("Student username: ")
        password = input("Student password: ")
        campus = input("Campus: ")

        if campus not in list(self.campuses.keys()):
            print("Not available campus")
            return

        campus = self.campuses.get(campus)
        if campus.has_free_slots():
            campus.add_student(Student(username, password))
            campus.slots -= 1
        else:
            print("Not available slots")

    def show_campuses_slots(self):
        for campus in list(self.campuses.values()):
            print(f"Campus: {campus.name}, slots: {campus.slots}")
