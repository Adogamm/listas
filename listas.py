'''
Alumno: Adolfo León Barrón
Materia: Estructura de datos
Practica: Listas 1
'''
from time import sleep
import os

lista=[]
while True:
    os.system("cls")
    print("¿Que desea hacer?")
    print('1) Inserciones')
    print('2) Consulta')
    print('3) Ordenar')
    print('4) Eliminar')
    print('5) Salir')
    accion = int(input("Ingresa el numero de tu operacion: "))
    os.system("cls")

    if accion == 1:
        inserciones = int(input("¿Cuantos registros vas a hacer? "))
        os.system("cls")
        while inserciones != 0:
            nombre = str(input("Ingresa el nombre del alumno: "))
            lista.append(nombre)
            inserciones = inserciones-1

        print("")
        for i in lista:
            print(i)
        print("")

    if accion == 2:
        consulta = str(input("Ingresa el nombre a buscar: "))
        if consulta in lista:
            print("")
            print("El alumno fue encontrado en la posicion: ",(lista.index(consulta)+1))
            print("")
        else:
            print("")
            print("Alumno no encontrado")
            print("")
        sleep(5)
        os.system("cls")

    if accion == 3:
        print("Ingresa un numero para seleccionar la operacion: ")
        print("1) El orden contrario al del registro")
        print("2) Ascendente")
        print("3) Descendente")
        ordenar = int(input("¿Como se van a ordenar los datos: "))
        os.system("cls")

        if ordenar == 1:
            lista.reverse()
        elif ordenar == 2:
            lista.sort()
        elif ordenar == 3:
            lista.sort(reverse=True)
        else:
            print("Operacion no valida")

        print("")
        for i in lista:
            print(i)
        print("")

    if accion == 4:
        print("Tipo de eliminacion")
        print("1) El ultimo dato registrado")
        print("2) Por indice")
        print("3) Un dato especifico")
        eliminacion = int(input(""))
        os.system("cls")

        if eliminacion == 1:
            lista.pop()
        elif eliminacion == 2:
            indice = int(input("Ingresa el indice del dato a eliminar "))
            lista.pop(indice)
        elif eliminacion == 3:
            dato = str(input("Ingresa el nombre del alumno que deseas eliminar "))
        else:
            print("Operacion no valida")

        if lista == []:
            print("")
            print("================== No hay nada ==============")
            print("")
        else:
            print("")
            for i in lista:
                print(i)
            print("")

    if accion == 5:
        print("|===| H A S T A   L U E G O |===|")
        break
