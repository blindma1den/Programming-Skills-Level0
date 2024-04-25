import os
import csv

def create_csv_file(file_path):
    encabezados = ['user_name', 'destinatario', 'ciudad',
                   'pais', 'peso', 'precio', 'fecha_envio', 'fecha_llegada']

    if not os.path.isfile(file_path):
        with open(file_path, 'w') as file:
            file.write(','.join(encabezados) + '\n')
    else:
         return True


def export_csv(user_name, addressee_details_list, peso, precio, fecha_envio, fecha_llegada, file_path):
        name = addressee_details_list[0]
        last_name = addressee_details_list[1]
        city = addressee_details_list[2]
        country = addressee_details_list[3]

        destinatario = f'{name} {last_name}'
        data = [user_name, destinatario, city, country, str(peso), str(precio), fecha_envio, fecha_llegada]
        
        with open(file_path, 'a', newline='') as file:
             writer = csv.writer(file)
             writer.writerow(data)




