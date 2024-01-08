from models import Program


class University:

    programs: dict[str, Program]

    def __init__(self, programs):
        self.programs = programs

    def show_programs(self):
        for index, program in enumerate(list(self.programs.values())):
            print("-"*20)
            print(f"{index+1}. {program.name}")
            print(program.show_campuses_slots())
            print("-"*20)

    def register_student(self):
        self.show_programs()
        program_name = input("Program: ")
        if program_name not in list(self.programs.keys()):
            print("Not available program")

        program = self.programs.get(program_name)
        program.register_student()

    def menu(self):
        print("1. Show programs")
        print("2. Register student")
        print("3. Exit")
        option = int(input("Option: "))
        return option
