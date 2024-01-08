from models.University import University
from models.Campus import Campus
from models.Program import Program


def load_campus_config():
    london = Campus(name="London", slots=1)
    manchester = Campus(name="Manchester", slots=3)
    liverpool = Campus(name="Liverpool", slots=1)
    computer_science = Program(name="Computer Science")
    medicine = Program(name="Medicine")
    marketing = Program(name="Marketing")
    arts = Program(name="Arts")
    programs = [computer_science, medicine, marketing, arts]
    programs_dict = {}
    for program in programs:
        program.add_campus(london)
        program.add_campus(manchester)
        program.add_campus(liverpool)
        programs_dict.update({program.name: program})

    return programs_dict


def main():

    programs = load_campus_config()
    university: University = University(programs)

    loop: bool = True

    while loop:
        option = university.menu()
        if option == 1:
            university.show_programs()
        elif option == 2:
            university.register_student()
        else:
            loop = False


if __name__ == "__main__":
    main()
