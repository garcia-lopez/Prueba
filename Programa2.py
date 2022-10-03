from Problema1 import Lista as listado
lst = listado()

def recursividad(pos):
    prueba = listado.retornarPaciente(pos)
    print(prueba)
    recursividad(pos)