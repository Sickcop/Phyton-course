grados = int(input("Ingresa número de grados: "))
unidad = input("Ingresa la unidad (C) o (F): ").lower()

numeroF = (grados)


if unidad == "f":
    resultadoUno = (grados- 32) * 5/9
    print(resultadoUno)
    
elif unidad == "c":
    resultadoDos = (grados * 9/5) + 32
    print(resultadoDos)

else:
    print("Unidad incorrecta")





