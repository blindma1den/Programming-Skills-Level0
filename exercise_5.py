"""5. Develop a finance management application with the following features:
* 	The user records their total income.
* 	There are categories: Medical expenses, household expenses, leisure, savings, and education.
* 	The user can list their expenses within the categories and get the total for each category.
* 	The user can obtain the total of their expenses.
* 	If the user spends the same amount of money they earn,
 the system should display a message advising the user to reduce expenses in the category where they have spent the most money.
* 	If the user spends less than they earn,
 the system displays a congratulatory message on the screen.
* 	If the user spends more than they earn,
 the system will display advice to improve the user's financial health."""


medical_expenses = []
household_expenses = []
laisure_list = []
saving_list = []
education_list = []


def medical(medical_expenses):
    medical_expenses_join = int(input("Medical expenses> "))
    medical_expenses.append(medical_expenses_join)
    print(medical_expenses)

def household(household_expenses):
    household_expenses_join = int(input("household expenses: "))
    household_expenses.append(household_expenses_join)
    print(household_expenses)

def laisure(laisure_list):
    laisure_join = int(input("join laisure expenses: "))
    laisure_list.append(laisure_join)
    print(f"you expensis are {laisure_list}")

def saving(saving_list):
    saving_join = int(input("enter saiving money: "))
    saving_list.append(saving_join)
    print(saving_list)

def education(education_list):
    education_join = int(input("entry you education expenses: "))
    education_list.append(education_join)
    print(education_list)

def record_income(education,saving,laisure,household,medical):
    print("Insert your expenses by category...")
    med = medical(medical_expenses)
    hous = household(household_expenses)
    lai = laisure(laisure_list)
    sav = saving(saving_list)
    edu = education(education_list)
    print(med,hous,lai,sav,edu)

def sum_lists(*lists):
    # Verifica que todas las listas tengan la misma longitud
    list_lengths = set(len(lst) for lst in lists)
    if len(list_lengths) != 1:
        raise ValueError("All input lists must have the same length.")

    result = [sum(lst) for lst in lists]
    return result

def analyze_financial_health(medical_expenses,household_expenses,laisure_list,saving_list,education_list,salary_neto):
    categories = [
        ("Gastos médicos", sum(medical_expenses)),
        ("Gastos del hogar", sum(household_expenses)),
        ("Gastos de ocio", sum(laisure_list)),
        ("Gastos de ahorros", sum(saving_list)),
        ("Gastos de educación", sum(education_list))
    ]

    for category, total_expense in categories:
        status = "Good" if total_expense < salary_neto else "Not good"
        print(f"{category}: {status}")

def menu():
    print("Menu")
    print("1----Insert you expenses by categories")
    print("2----calculate you expenses")
    print("3----Recomendations")
    print("4----exit")



print("Finance Management Application")
print()

salary_neto = int(input("Join your salary> "))
print(salary_neto)

while True:
    menu()
    choice = input("Select one option (1-4): ")

    if choice == '1':
        income = record_income(education,saving,laisure,household,medical)
    elif choice == '2':
        result_list = sum_lists(medical_expenses, household_expenses, laisure_list,saving_list,education_list)
        print("Sum of lists:", result_list)
    elif choice == '3':
        analyze_financial_health(medical_expenses,household_expenses,laisure_list,saving_list,education_list,salary_neto)
    elif choice == '4':
        print("¡Good Bye!")
        break
    else:
        print("Error 404.")
        break



