from datetime import datetime
def valid_int(value):
    ''' Funcion para validar números enteros '''
    while True:
        try:
            dato = int(input(value))
            return dato
        except ValueError:
            print("Ingrese un dato válido (números enteros)")
def valid_float(value):
    ''' Funcion para validar números flotantes '''
    while True:
        try:
            dato = float(input(value))
            return dato
        except ValueError:
            print("Ingrese un dato válido (números flotantes)")
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
def validar_date(msj):
    while True:
        print("Ingrese la fecha en la que se realizó el estudio")
        print("Ingrese el día: ")
        dia = valid_int(msj)

        print("Ingrese el mes: ")
        mes = valid_int(msj)

        print("Ingresar el año: ")
        año = valid_int(msj)

        try:
            fecha = datetime(año, mes, dia)
            break
        except ValueError:
            print("Fecha incorrecta, ingrese la fecha de nuevo")
    print("Fecha: ", fecha.strftime("%d/%m/%Y"))
    return str(fecha)

class Medicamento:
    def __init__(self):
        #se crean atributos privados(__)
        self.__nombre="" 
        self.__dosis= 0 

    #Getters
    def verNombre(self): #Polimorfismo
        return self.__nombre
    def verDosis(self):
        return self.__dosis

    #Setters
    def asignarNombreMed(self,med):
        self.__nombre = med  
    def asignarDosis(self, cant):
        self.__dosis = cant     
class Mascota:
    #metodo init para inicializar la clase
    def __init__(self):
        self.__nombre= " "
        self.__historia = 0
        self.__tipo = " "
        self.__peso = " "
        self.__fecha_ingreso = " "
        self.__lista_medicamentos = [] #se crea un elemento contenedor privado (lista) para almacenar los medicamentos
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        #Creamos elementos contenedores (diccionarios)
        self.__listaCaninos = {}
        self.__listaFelinos = {}
    
    def verificarExiste(self,historia):
        for m in self.__listaCaninos.values():
            if historia == m.verHistoria():
                return True
    
        for m in self.__listaFelinos.values():
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self):
        cantidadCaninos = len(self.__listaCaninos)
        cantidadFelinos = len(self.__listaFelinos)
        total = cantidadCaninos + cantidadFelinos
        return total
    
    def ingresarMascota(self,mascota):
        historia= mascota.verHistoria()
        if mascota.verTipo() == "felino":
            self.__listaFelinos[historia] = mascota
        elif mascota.verTipo() == "canino":
            self.__listaCaninos[historia] = mascota
        else:
            print("Ingreso una opcion invalida")
   

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__listaCaninos.values():
            if historia == masc.verHistoria():
                return masc.verFecha() 
        for masc in self.__listaFelinos.values():
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__listaCaninos.values():
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos()
        for masc in self.__listaFelinos.values():
            if historia == masc:
                return masc.verLista_Medicamentos()
        return None
    
    def eliminarMascota(self, historia):
        if historia in self.__listaFelinos:
            mascota_eliminada = self.__listaFelinos.pop(historia)
            return True  #eliminado con exito
        if historia in self.__listaCaninos:
            mascota_eliminada = self.__listaCaninos.pop(historia)
            return True  #eliminado con exito
        return False
        
    def eliminarMedicamento(self, historia):
        for mascota in self.__listaCaninos.values():
            if historia == mascota.verHistoria():
                mascota.asignarLista_Medicamentos([])
                return True
        
        for mascota in self.__listaFelinos.values():
            if historia == mascota.verHistoria():
                mascota.asignarLista_Medicamentos([])
                return True

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=valid_int('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Eliminar medicamento
                       \n7- Salir 
                       \nUsted ingresó la opción: ''' )
        if menu == 1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=valid_int("Ingrese la historia clínica de la mascota: ")
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=valid_letter("Ingrese el nombre de la mascota: ")
                tipo=valid_letter("Ingrese el tipo de mascota (felino o canino): ")
                peso=valid_float("Ingrese el peso de la mascota: ")
                fecha=validar_date("Ingrese la fecha de ingreso (dia/mes/año): ")
                nm=valid_int("Ingrese cantidad de medicamentos: ")
                lista_med=[]

                for i in range(0,nm):
                    nombre_medicamentos = valid_letter("Ingrese el nombre del medicamento: ")

                    med_repetido= False
                    for medicamento in lista_med:
                        if nombre_medicamentos==medicamento.verNombre():
                            print("No se puede ingresar,  medicamento ya estaba recetado")
                            med_repetido = True
                            break

                    if med_repetido:
                        continue

                    dosis =valid_int("Ingrese la dosis: ")
                    medicamento = Medicamento()
                    medicamento.asignarNombreMed(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

                print("Macota guardada con exito")

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu == 2: # Ver fecha de ingreso
            h = valid_int("Ingrese la historia clínica de la mascota: ")
            fecha = servicio_hospitalario.verFechaIngreso(h)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu == 3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu == 4: # Ver medicamentos que se están administrando
            h = valid_int("Ingrese la historia clínica de la mascota: ")
            medicamento = servicio_hospitalario.verMedicamento(h) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            h = valid_int("Ingrese la historia clínica de la mascota: ")
            resultado_operacion = servicio_hospitalario.eliminarMascota(h) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")

        elif menu == 6:
            h = valid_int("Ingrese la historia clínica de la mascota: ")
            resultado_operacion = servicio_hospitalario.eliminarMedicamento(h)

            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")

        
        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

        

if __name__=='__main__':
    main()





            

                

