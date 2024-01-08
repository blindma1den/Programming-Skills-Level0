from models import Student


class Campus:

    slots: int
    students: list[Student]
    name: str

    def __init__(self, slots: int, name: str):
        self.slots = slots
        self.name = name
        self.students = []

    def has_free_slots(self):
        return self.slots > 0

    def add_student(self, student: Student):
        self.students.append(student)


