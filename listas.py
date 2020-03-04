'''
Alumno: Adolfo León Barrón
Materia: Estructura de datos
Practica: Listas 1
'''
from time import sleep

lista=[]
inserciones = int(input("¿Cuantos registros vas a hacer? "))
while inserciones != 0:
    nombre = str(input("Ingresa el nombre del alumno: "))
    lista.append(nombre)
    inserciones = inserciones-1

print("")
for i in lista:
    print(i)
print("")

consulta = str(input("Ingresa el nombre a buscar: "))
if consulta in lista:
    print("")
    print("El alumno fue encontrado en la posicion: ",(lista.index(consulta)+1))
    print("")
else:
    print("")
    print("Alumno no encontrado")
    print("")

print("Ingresa un numero para seleccionar la operacion: ")
print("1) El orden contrario al del registro")
print("2) Ascendente")
print("3) Descendente")
ordenar = int(input("¿Como se van a ordenar los datos: "))

if ordenar == 1:
    lista.reverse()
elif ordenar == 2:
    lista.sort
elif ordenar == 3:
    lista.sort(reverse=True)
else:
    print("Operacion no valida")

print("")
for i in lista:
    print(i)
print("")

print("Tipo de eliminacion")
print("1) El ultimo dato registrado")
print("2) Por indice")
print("3) Un dato especifico")
eliminacion = int(input(""))

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
