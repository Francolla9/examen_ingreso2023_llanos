import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:


A)  Al presionar el botón 'Agregar' se deberan cargar tantos vehiculos como el usuario desee. 
    Los datos a cargar de cada vehiculo son: marca (ford, volvo, fiat), tipo de vehiculo (auto, camioneta, moto) y kilometros*.

* Todos los autos son usados.

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar se deberan listar todos los vehiculos ingresados con su correspondiente kilometraje y su posicion en la lista.
Ejemplo: 1 - Ford - Auto - 1000 km
         2 - Fiat - Camioneta - 2000 km
         etc..

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al presionar el boton Informar 
    0- El mayor kilometraje y su tipo de vehiculo.
    1- El menor kilometraje y su tipo de vehiculo de marca 'Ford'.
    2- Kilometraje promedio de los autos por cada marca.
    3- Precio promedios de todos los servicios por marca.
    4- Informar los kilometrajes que superan el promedio (total) por tipo.
    5- Informar los kilometrajes que NO superan el promedio (total) por marca.
    6- Informar la cantidad de tipos por marca.
    7- Informar el precio promedio de los servicios cuyo kilometraje es mayor a 10000 kms de marca 'Volvo'.
    8- Indicar el mayor de los promedios de kilometros por tipo de vehiculo.
    9- Informar el monto promedio de los servicios de marca 'Ford'.


Los montos de los servicios son:
    - Auto: $15000
    - Camioneta: $25000
    - Moto: $10000
    
    *Si la marca es volvo tiene un recargo del 10%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("EXAMEN INGRESO")
        
        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_tipo_vehiculo = []
        self.lista_marca_vehiculo = []
        self.lista_kms_vehiculos = []

    def btn_agregar_on_click(self):
        respuesta = "s"
        
        while respuesta =="s":

            marca = prompt("ingreso","ingrese una marca")

            while marca != "ford" and marca != "volvo" != marca !=  "fiat": 
                alert("error","error en la carga")
                marca = prompt("ingreso","ingrese una marca") 

            alert("exitos","el vehiculo fue ingresado correctamente")
            self.lista_marca_vehiculo.append(marca)

            tipo_vehiculo = prompt("ingreso","ingrese un tipo de vehiculo")

            while not tipo_vehiculo.isdigit() and tipo_vehiculo != "auto" and tipo_vehiculo != "moto" and tipo_vehiculo != "camioneta":
                alert("error","error en la carga")
                tipo_vehiculo = prompt("ingreso","ingrese un tipo de vehiculo")

            alert("excelente","el ingreso es valido")
            self.lista_tipo_vehiculo.append(tipo_vehiculo)


            kilometros = prompt("ingreso","ingrese los km correspondientes")

            while not kilometros.isdigit() or int(kilometros) <=0: 
                alert("error","error en la carga") 
                kilometros = prompt("ingreso","ingrese los km correspondientes")

            alert("excelente","el dato ingreso")  
            self.lista_kms_vehiculos.append(kilometros)   
            kilometros = int(kilometros)    
  


            respuesta = prompt("hola","desea ingresar otro vehiculo?(s/n)")
            while respuesta != "s" and respuesta != "n":
                respuesta = prompt("hola","desea ingresar otro vehiculo?(s/n)")


    
    def btn_mostrar_on_click(self):
        for i in range(0,len(self.lista_kms_vehiculos),1):
            print("la posicion es" , i , " el vehiculo es" , self.lista_tipo_vehiculo[i], " , tiene ",self.lista_kms_vehiculos[i], "kilometros y es marca",self.lista_marca_vehiculo[i])


    def btn_informar_on_click(self):
    #consigna 6

        contador_tipo_marca = 0
        for i in range(0,len(self.lista_tipo_vehiculo),1):
            contador_tipo_marca += 1
            i = contador_tipo_marca
            print(i , self.lista_tipo_vehiculo[i], self.lista_marca_vehiculo[i])

    #consigna 3 


        
        
    
        



       

       
if __name__ == "__main__":
    app = App()
    app.geometry("200x400")
    app.mainloop()

