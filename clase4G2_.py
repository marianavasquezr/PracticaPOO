#Funcion para validar enteros
def valid_int(value):
    ''' Funcion para validar números enteros '''
    while True:
        try:
            dato = int(input(value))
            return dato
        except ValueError:
            print("Ingrese un dato válido (números enteros)\n")

#Creamos la clase paciente
class Paciente:
    #Creamos el método constructor de Paciente para incializar sus atributos
    def __init__(self):
      self.__nombre = ""
      self.__cedula = 0
      self.__genero = ""
      self.__servicio = ""
    #Getters  
    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    #Setters
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

#Creamos la clase sistema
class Sistema:
    #Creamos el constructor de la clase sistema
    def __init__(self):
      #Creamos un contenedor vacio, en este caso una lista, para ir añadiendo los objetos pacientes que van ingresando al sistema
      self.__lista_pacientes = []
      #Usamos el método len de lista para ver la cantidad de pacientes que hay agregados
      self.__numero_pacientes = len(self.__lista_pacientes)
      
    def ingresarPaciente(self):
        # 1- solicito los datos por teclado
        nombre = input("Ingrese el nombre: ")
        cedula = int(input("Ingrese la cedula: "))    
        genero = input("Ingrese el genero: ")
        servicio = input("Ingrese el servicio: ")
        # 2- creo el objeto Paciente y le asigno los datos
        p = Paciente()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)        
        # 3- guardo el Paciente en  la lista        
        self.__lista_pacientes.append(p)
        # self.__lista_pacientes[p.verCedula()] = p
        # 4- actualizo la cantidad de pacientes en el sistema
        self.__numero_pacientes = len(self.__lista_pacientes)

    def verNumeroPacientes(self):
        #print(f"En el sistema se encuentran {len(self.__lista_pacientes)} pacientes.")
        return self.__numero_pacientes
    
    
    def verDatosPaciente(self):
        cedula = int(input("Ingrese la cedula a buscar: "))
        #La variable paciente recorre la lista de pacientes
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                #Bandera
                verif = True
                #Si la cedula solicitada está, muestra la informacion de paciente en pantalla
                print("Nombre: " + paciente.verNombre())
                print("Cedula: " + str(paciente.verCedula()))
                print("Genero: " + paciente.verGenero())
                print("Servicio: " + paciente.verServicio())
            else:
                verif = False
        if verif == False:
            print("\nEl paciente no se encuentra registrado en el sistema.")

                
#Definimos la funcion main 
def main():
    #Crear una instancia de la clase sistema para tomar sus atributos y funciones para modificarlos
    a= Sistema()
    #a.ingresarPaciente()

    while True:
        menu= int(input("""\n Ingrese una opción:
                   1. Ingresar paciente
                   2. Numero de pacientes ingresados
                   3. Datos del paciente
                   4. Salir
                   """))
        
        if menu == 1:
            pass
        elif menu== 2:
            pass
        elif menu == 3:
            pass
        elif menu == 4:
            print("Saliendo del sistema, gracias por utilizar nuestros servicios ")
            break


#Llamamos la funcion main para que identifique el archivo que se esta ejecutando 
if __name__=="__main__":
    main()
