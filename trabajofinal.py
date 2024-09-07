#*********************************************************//////////////////////****************************************************
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo 2 trabajo final  mejoradooooooooooooooooooooooooooooooooooooooooooooooooooo
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooo0 2 trabajo final  mejoradooooooooooooooooooooooooooooooooooooooooooooooooooo

"""Esto programa  gestiona datos de alumnos de catequesis en una  una vicaria.
 El programa : 
 a)Llevar un registro de todos los datos de alumnos de la catequesis (Dni,Nombre,  Apellido, fecha de nacimiento,
 Nombre de Tutor,  sacramentos recibidodo, en un diccionario para almacena modificar muestra, y eliminar los datos de los alumnos 
b)dentro de un menu desplegable  que contiene 
Archivo : salir , 
Alumnos : Alumnos de comunion: agregar, modificar, eliminar , mostrar alumnos ,
          Alumnos de confirmacion :agregar, modificar, eliminar , mostrar alumnos.
Ayuda= version y quien lo creo """


import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import re
#import tkinter

class catequesis:
    def __init__(self, root):
        self.root = root
        self.root.title( "VICARIA  NTRA.SEÑORA DE GUADALUPE - ALUMNOS DE CATEQUESIS 2024 ")
        self.root.geometry("1000x600" )
        self.root.config(bg="orange")
        self.root.resizable(0,0)
        self.root.mainloop
 
        self.alumnos = {}
        self.alumnos_conf={}

        # Menú
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        archivo_menu = tk.Menu(menu, tearoff=1)

        archivo_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Archivo ", menu=archivo_menu)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.root.quit)
             
        alumnos_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Alumnos", menu=alumnos_menu)  
        comunion_menu = tk.Menu(alumnos_menu, tearoff=0)
        alumnos_menu.add_cascade(label="Alumnos de Comunión", menu=comunion_menu)
        comunion_menu.add_command(label="Agregar Alumnos de comunión", command=self.agregar_alumno)
        comunion_menu.add_command(label="Modificar Alumnos de comunión", command=self.modificar_alumno)
        comunion_menu.add_command(label="Eliminar Alumnos de comunión", command=self.eliminar_alumno)
        comunion_menu.add_command(label="Mostrar Alumnos de comunión", command=self.mostrar_alumnos)


        confirmacion_menu = tk.Menu(alumnos_menu, tearoff=0)
        alumnos_menu.add_cascade(label="Alumnos de Confirmación", menu=confirmacion_menu)
        confirmacion_menu.add_command(label="Agregar Alumnos de Confirmación", command=self.agregar_alumno_conf)
        confirmacion_menu.add_command(label="Modificar Alumnos de Confirmación", command=self.modificar_alumno_conf)
        confirmacion_menu.add_command(label="Eliminar Alumnos de Confirmación ", command=self.eliminar_alumno_conf)
        confirmacion_menu.add_command(label="Mostrar Alumnos de Confirmación ", command=self.mostrar_alumnos_conf)

        ayuda_menu=tk.Menu(menu,tearoff=0)
        ayuda_menu.add_command(label="Versión", command=self.mostrar_version)
        menu.add_cascade (label="ayuda", menu=ayuda_menu)

        #COMIENZO A TRABAJAR CON los alumnos de comunion definiendo primero las funciones para agregar -modificar-eliminar-mostrat alumnos

    def agregar_alumno(self):
       self.alumno_de_comunion(" Alumnos de Comunión agregado")
    
    def modificar_alumno(self):
        self.alumno_de_comunion("Alumno de Comunión modificado")

    def eliminar_alumno(self):
        self.alumno_de_comunion(" Alumno de comunión elimonado")
        dni = self.obtener_dni()
        if dni in self.alumnos:
            del self.alumnos[dni]
            messagebox.showinfo("Éxito", "Alumno de comunion eliminado correctamente")
        else:
            messagebox.showerror("Error", "Alumno de comunion no encontrado")

    def mostrar_alumnos(self):
        alumnos_str = "\n".join([f"{dni}: {datos}" for dni, datos in self.alumnos.items()])
        messagebox.showinfo("Alumnos comunion registrados", alumnos_str if alumnos_str else "No hay alumnos registrados")

                
    def alumno_de_comunion (self, accion):

        form = tk.Toplevel(self.root)
        form .title(accion)

        tk.Label(form, text="DNI").grid(row=0, column=0)
        dni_entry = tk.Entry (form)
        dni_entry.grid(row=0, column=1)

        tk.Label(form, text="Nombre").grid(row=1, column=0)
        nombre_entry = tk.Entry(form)
        nombre_entry.grid(row=1, column=1)

        tk.Label(form, text="Apellido").grid(row=2, column=0)
        apellido_entry = tk.Entry(form)
        apellido_entry.grid(row=2, column=1)

        tk.Label(form, text="Fecha de Nacimiento(DD/MM/AA)").grid(row=3, column=0)
        fecha_nacimiento_entry = tk.Entry(form)
        fecha_nacimiento_entry.grid(row=3, column=1)

        tk.Label(form, text="Nombre del Tutor").grid(row=4, column=0)
        tutor_entry = tk.Entry(form)
        tutor_entry.grid(row=4, column=1)

        tk.Label(form, text="Sacramentos Recibidos").grid(row=5, column=0)
        sacramentos_entry = tk.Entry(form)
        sacramentos_entry.grid(row=5, column=1)
    
        def guardar():
            dni = dni_entry.get()
            nombre1=nombre_entry.get()
            apellido=apellido_entry.get()
            fecha=fecha_nacimiento_entry.get()
            nombretutor= tutor_entry.get()
            sacramentos=sacramentos_entry.get()
            
            self.alumnos[dni] = {
                "Nombre": nombre_entry.get(),
                "Apellido": apellido_entry.get(),
                "Fecha de Nacimiento": fecha_nacimiento_entry.get(),
                "Nombre del Tutor": tutor_entry.get(),
                "Sacramentos Recibidos": sacramentos_entry.get()
            }
            if not dni.isdigit():
                 messagebox.showerror("Error", "DNI debe ser un número.")
            else:
                 messagebox.showinfo("Éxito", f"{accion.lower()} guardao correctamente")
                 form.destroy()
               #  tk.Button(form, text="Guardar", command=guardar).grid(row=6, columnspan=2)
                 return
               
            if not nombre1.isalpha():
                messagebox.showerror("Error", "Nombre debe contener solo letras.")
                return
                        
            if not apellido.isalpha():
                messagebox.showerror("Error", "Apellido debe contener solo letras.")
                return
                
            if not nombretutor.isalpha():
                messagebox.showerror("Error", "tutor debe contener solo letras.")
                return
            if not sacramentos.isalpha():
                messagebox.showerror ("Error", "el sacramento debe contener solo letras.")
                return
            if not re.match(r"\d{2}/\d{2}/\d{2}", fecha):
                messagebox.showerror("Error", "Fecha de Nacimiento debe estar en formato dd/mm/yy")
            return False
            #try:
                #formato="%dd -%mm -%yy"
              #datetime.strptime(fecha, formato)
            #except ValueError:
             #   messagebox.showerror("Error", "Fecha de nacimiento debe tener el formato DD-MM-AA.")
        tk.Button(form, text="Guardar", command=guardar).grid(row=6, columnspan=2)
        return

            #_________________________#_________________________________________________________________________
        #comienzo a trabajar con el menu de confirmacion  

    def agregar_alumno_conf(self):
            self.alumno_form_conf(" Alumnos de confirmacion agregado ")


    def modificar_alumno_conf(self):
        self.alumno_form_conf(" Alumno de Confirmacion modificado ")


    def eliminar_alumno_conf(self): 
        self.alumno_form_conf(" Alumno de confirmacion eliminado")
        dni = self.obtener_dni()

        if dni in self.alumnos_conf:
            del self.alumnos_conf[dni]
            messagebox.showinfo("Éxito", "Alumno eliminado correctamente")
        else:
            messagebox.showerror("Error", "Alumno no encontrado")

    def mostrar_alumnos_conf(self):

        alumnos_str = "\n".join([f"{dni}: {datos}" for dni, datos in self.alumnos_conf.items()])

        messagebox.showinfo("Alumnos confirmacion registrados", alumnos_str if alumnos_str else "No hay alumnos registrados")

      
    def alumno_form_conf(self, accion):

        form = tk.Toplevel(self.root)                                  
        form.title(accion)

        tk.Label(form, text="DNI").grid(row=0, column=0)
        dni_entry = tk.Entry(form)
        dni_entry.grid(row=0, column=1)

        tk.Label(form, text="Nombre").grid(row=1, column=0)
        nombre_entry = tk.Entry(form)
        nombre_entry.grid(row=1, column=1)

        tk.Label(form, text="Apellido").grid(row=2, column=0)
        apellido_entry = tk.Entry(form)
        apellido_entry.grid(row=2, column=1)

        tk.Label(form, text="Fecha de Nacimiento").grid(row=3, column=0)
        fecha_nacimiento_entry = tk.Entry(form)
        fecha_nacimiento_entry.grid(row=3, column=1)

        tk.Label(form, text="Nombre del Tutor").grid(row=4, column=0)
        tutor_entry = tk.Entry(form)
        tutor_entry.grid(row=4, column=1)

        tk.Label(form, text="Sacramentos Recibidos").grid(row=5, column=0)
        sacramentos_entry = tk.Entry(form)
        sacramentos_entry.grid(row=5, column=1)

        def guardar_alumnos_conf():
            dni = dni_entry.get()
            nombre1=nombre_entry.get()
            apellido=apellido_entry.get()
            fecha=fecha_nacimiento_entry.get()
            nombretutor= tutor_entry.get()
            sacramentos=sacramentos_entry.get()
            
            self.alumnos_conf[dni] = {
                "Nombre": nombre_entry.get(),
                "Apellido": apellido_entry.get(),
                "Fecha de Nacimiento": fecha_nacimiento_entry.get(),
                "Nombre del Tutor": tutor_entry.get(),
                "Sacramentos Recibidos": sacramentos_entry.get()
            }
            if not dni.isdigit():
                 messagebox.showerror("Error", "DNI debe ser un número.")
            else:
                 messagebox.showinfo("Éxito", f" {accion.lower()} guardado correctamente")
                 form.destroy()
                 tk.Button(form, text="Guardar", command=guardar_alumnos_conf).grid(row=6, columnspan=2)
                 return
               
            if not nombre1.isalpha():
                messagebox.showerror("Error", "Nombre debe contener solo letras.")
                return
                        
            if not apellido.isalpha():
                messagebox.showerror("Error", "Apellido debe contener solo letras.")
                return
                
            if not nombretutor.isalpha():
                messagebox.showerror("Error", "tutor debe contener solo letras.")
                return
            if not sacramentos.isalpha():
                messagebox.showerror ("Error", "el sacramento debe contener solo letras.")
                return
            if not re.match(r"\d{2}/\d{2}/\d{2}", fecha):
                messagebox.showerror("Error", "Fecha de Nacimiento debe estar en formato dd/mm/yy")
            return False
                    
            
        tk.Button(form, text="Guardar", command=guardar_alumnos_conf).grid(row=6, columnspan=2)
        return

        
    def mostrar_version(self):
        menu = tk.Menu(self.root)
        messagebox.showinfo("Versión", "Versión 1.0\nCreado por Clarisa Cardoso")
        ayuda_menu=tk.Menu(menu,tearoff=0)
        ayuda_menu.add_command(label="Versión", command=self.mostrar_version)
        menu.add_cascade (label="ayuda", menu=ayuda_menu)

if __name__ == "__main__":
    root = tk.Tk()
    app = catequesis(root)
    root.mainloop()

