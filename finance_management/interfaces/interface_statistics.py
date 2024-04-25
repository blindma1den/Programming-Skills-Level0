

def interface_general_evaluation(result, total_income, total_expenses):
    mensaje = "Evaluación final"
    print("="*len(mensaje))
    print(mensaje)
    print("")
    print(f"Total de ingresos: {total_income}")
    print(f"Total de gastos: {total_expenses}")
    print("="*len(mensaje))
    print("Conclusión: ")
    print(result)
    print("="*len(mensaje))
    

def interface_means(mean_list):
    print("=" * 20)
    print("Promedio por categoría")
    print("=" * 20)
    print("Gastos médicos: ", mean_list[0])
    print("Gasto del hogar: ", mean_list[1])
    print("Ocio: ", mean_list[2])
    print("Ahorro: ", mean_list[3])
    print("Educación: ", mean_list[4])
    print("Otros: ", mean_list[5])
    print("=" * 20)
    print("\n")