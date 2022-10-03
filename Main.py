from Problema1 import Paciente as persona, Lista as listado
import Programa2 as programa
registro = listado()


def registrasPacientes():
    nom = input("Nombre del paciente: ")
    ed = int(input("Edad del paciente: "))
    fechIn = input("Fecha de ingreso: ")
    dom = input("Domicilio: ")

    elemento = persona(nom, ed, fechIn, dom)
    registro.agregarPaciente(elemento)


def imprimirPacientesEdades():
    registro.edadesPacientes()


def imprimirPacientes():
    registro.imprimirPaciente()


def programaAlReves():
    pos = len(registro.pacientes) - 1
    programa.recursividad(pos)


def menu():
    print("-----Opciones-----")
    print("1. Agregar Paciente")
    print("2. Imprimir todos los pacientes")
    print("3. Imprimir los pacientes por rango de edad")
    print("4.Imprimir Pacientes del último al primero")
    print("5. ---Cerrar---")

    op = int(input("Opcion elegida >> "))

    return op


def main():
    op = 0
    while (op != 5):
        op = menu()
        if (op == 1):
            registrasPacientes()
        elif (op == 2):
            imprimirPacientes()
        elif (op == 3):
            imprimirPacientesEdades()
        elif (op == 4):
            programaAlReves()

        elif (op == 5):
            print("Ha cerrado el programa")

        else:
            print("Intente nuevamente")


main()
