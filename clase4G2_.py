#Funcion para validar enteros
def valid_int(value):
    ''' Funcion para validar números enteros '''
    while True:
        try:
            dato = int(input(value))
            return dato
        except ValueError:
            print("Ingrese un dato válido (números enteros)\n")
def valid_letter(question):
    import re
    ''' Valida que el dato ingresado sea de caracteres alfabetico, 
    incluyendo tildes, mayusculas, minusculas, espacio sin aceptar caracteres especiales o números '''
    while True:
        txt = input(question)
        try:
            if re.match("^[a-zA-Z-ñÑ-áÁéÉíÍóÓúÚ ]*$", txt):
                return txt
            else:
                print("Ingresó caracteres especiales o números")
        except ValueError:
            print("\nIngrese solo letras y espacios, intente de nuevo")
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
    def verificarPaciente(self,cedula):
        #Bandera
        encontrado= False
        #Voy a buscar paciente por paciente
        for p in self.__lista_pacientes:
            #Por cada paciente de la lista, le digo al paciente que me retorne la cedula y la comparo con la ingresada por teclado
            if cedula == p.verCedula():
                encontrado = True #Si lo encuentra actualiza la bandera
                break #salgo del for
        return encontrado

    def ingresarPaciente(self, pac):
        if self.verificarPaciente(pac.verCedula()): #verifico primero si existe
            return False
        self.__lista_pacientes.append(pac)
        # 4- actualizo la cantidad de pacientes en el sistema
        self.__numero_pacientes = len(self.__lista_pacientes)
        return True

    def verNumeroPacientes(self):
        #print(f"En el sistema se encuentran {len(self.__lista_pacientes)} pacientes.")
        return self.__numero_pacientes
    
    
    def verDatosPaciente(self):
        cedula = valid_int("Ingrese la cedula a buscar: ")
        #La variable paciente recorre la lista de pacientes
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                #Bandera
                verif = True
            else:
                verif = False
        if verif == True:
            #Si la cedula solicitada está, muestra la informacion de paciente en pantalla
                print("Nombre: " + paciente.verNombre())
                print("Cedula: " + str(paciente.verCedula()))
                print("Genero: " + paciente.verGenero())
                print("Servicio: " + paciente.verServicio())
        else:
            print("\nEl paciente no se encuentra registrado en el sistema.")

                
#Definimos la funcion main 
def main():
    #Crear una instancia de la clase sistema para tomar sus atributos y funciones para modificarlos
    sis= Sistema()
    #a.ingresarPaciente()

    while True:
        menu= valid_int("""\n Ingrese una opción:
                   1. Ingresar paciente
                   2. Numero de pacientes ingresados
                   3. Datos del paciente
                   4. Salir
                   """)
        if menu == 1:
            # 1- solicito los datos por teclado
            nombre = valid_letter("Ingrese el nombre: ")
            cedula = valid_int("Ingrese la cedula: ") 
            genero = valid_letter("Ingrese el genero: ")
            servicio = input("Ingrese el servicio: ")
            # 2- creo el objeto Paciente y le asigno los datos
            p = Paciente()
            p.asignarNombre(nombre)
            p.asignarCedula(cedula)
            p.asignarGenero(genero)
            p.asignarServicio(servicio)        
            ingresar = sis.ingresarPaciente(p)
            if ingresar == False:
                print("Ya existe un paciente con esa cedula.")
            else:
                print("Paciente ingresado")
        elif menu== 2:
            print("\nSeñor usuario usted ha seleccionado la opción ver cantidad de pacientes registrados en el sistema")
            print(f"En el sistema se encuentran registrados {sis.verNumeroPacientes()} pacientes")
        elif menu == 3:
            print("\nSeñor usuario usted ha seleccionado la opción ver datos del paciente, por favor diligencie los siguientes datos")
            info = sis.verDatosPaciente()
            print(info)
        elif menu == 4:
            print("Saliendo del sistema, gracias por utilizar nuestros servicios ")
            break


#Llamamos la funcion main para que identifique el archivo que se esta ejecutando 
if __name__=="__main__":
    main()
