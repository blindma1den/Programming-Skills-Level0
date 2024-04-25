

def add_expense_fn(category, expense, read_json_fn, write_json_fn, file_path):

    data = read_json_fn(file_path)

    # Agregar el gasto a la categoria correspondiente
    for dictionary in data:
        for categoria in dictionary:
            if categoria == category:
                dictionary[categoria].append(expense)

    write_json_fn(data, file_path)