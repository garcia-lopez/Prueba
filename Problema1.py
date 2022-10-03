class Paciente:
    def __init__ (self, nom, ed, feIn, dom):
        self.Nombre = nom
        self.Edad = ed
        self.FechaIngreso = feIn
        self.Domicilio = dom
        
    def __str__(self):
        return f"""Nombre {self.Nombre}
Edad: {self.Edad}
Fecha de Ingreso: {self.FechaIngreso}
Domicilio: {self.Domicilio}"""

class Lista:
    def __init__(self):
        self.pacientes = []
        
    def agregarPaciente(self, paci):
        try:
            self.pacientes.append(paci)
            papa = self.pacientes.pop()
            print(papa)
            
        except Exception as ex:
            print(str(ex))
            
    def edadesPacientes(self):
        try:
            conta = 0
            edades = 0
            for patient in self.pacientes:
                if patient.Edad > 20 and patient.Edad < 30:
                    print(patient)
                    conta+= 1
                    edades = edades + patient.Edad
                    
            promedio = edades / conta
            print("Promedio de edad de ese rango: ")
            print(promedio)
            
        except Exception as ex:
            print(str(ex))
            
         
    def imprimirPaciente(self):
        try:
            for patient in self.pacientes:
                print(patient)
            
        except Exception as ex:
            print(str(ex))
            
    def retornarPaciente(self, pos):
        if self.pacientes:
             compañero = self.pacientes.pop(pos)
             return compañero
        else:
            print("Lista vacia")
        
       
        
            
 
    
    