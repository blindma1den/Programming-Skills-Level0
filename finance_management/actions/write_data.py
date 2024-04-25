

def create_categories_fn(read_json_fn, write_json_fn, file_path):

    categories = {
        "Gasto medicos": [],
        "Gasto del hogar": [],
        "Ocio": [],
        "Ahorro": [],
        "Educacion": [],
        "Otros": []
    }

    data = read_json_fn(file_path)
    data.append(categories)
    write_json_fn(data, file_path)

    return True


