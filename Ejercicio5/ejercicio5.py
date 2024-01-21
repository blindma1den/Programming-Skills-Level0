# 5. Develop a finance management application with the following features:
# * The user records their total income.
# * There are categories: Medical expenses, household expenses, leisure, savings, and education.
# * The user can list their expenses within the categories and get the total for each category.
# * The user can obtain the total of their expenses.
# * If the user spends the same amount of money they earn, the system should display a message advising the user to reduce expenses in the category where they have spent the most money.
# * If the user spends less than they earn, the system displays a congratulatory message on the screen.
# * If the user spends more than they earn, the system will display advice to improve the user's financial health.
categorias = {"Salud":0,"Hogar":0,"Ocio":0,"Ahorro":0,"Educacion":0,}

print("¡Bienvenido/a a nuestra aplicación de manejo de dinero!")
ingresos= int( input("Por favor, ingrese la cantidad total de sus ingresos:"))
categorias["Salud"] = int(input("Ingrese sus gastos en salud: "))
categorias["Hogar"] = int(input("Ingrese sus gastos en el hogar: "))
categorias["Ocio"] = int(input("Ingrese sus en ocio: "))
categorias["Ahorro"] = int(input("Ingrese sus gastos en ahorro: "))
categorias["Educacion"] = int(input("Ingrese sus gastos en Educacion: "))
gastosTotales=0
categoriaMayorGasto=""
for categoria,gasto in categorias.items():
    gastoMayor=0
    gastosTotales += gasto
    if(gastoMayor < gasto):
        gastoMayor= gasto
        categoriaMayorGasto= categoria

print("log gastos totales fueron:" +str(gastosTotales) )
if(gastosTotales >ingresos):
    print("¡Alerta! Tus gastos han sido demasiado altos. Aquí tienes algunas recomendaciones para reducir tus gastos:")
    print("1. Revisa tu presupuesto y elimina gastos innecesarios.")
    print("2. Considera reducir tus gastos en la categoría de " + str(categoriaMayorGasto) + ".")
elif(gastosTotales<ingresos):
     print("¡Felicitaciones! Tiene un gasto adecuado de sus ingresos.")
elif gastoMayor==ingresos:
    print("Tiene unos gastos altos. Le recomendamos reducir sus gastos en la categoría "  + str(categoriaMayorGasto) +  " para tener una mejor salud financiera.")
    


