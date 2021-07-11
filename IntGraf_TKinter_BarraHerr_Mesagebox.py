"""
DESCRIPCION:
Esta es una aplicacion donde se utliza li libreria Tkinter para la creacion de una barra de menu
(interfaz de usuario que indica y presenta las opciones o herramientas de una aplicación informática, 
dispuestas en menús desplegables). A su vez tambien se utiliza el modulo messagebox
(acceso a cuadros de diálogo estándar de tk  ) de la libreria Tkinter 
para introducir mensajes en las distintas opociones (mensajes de informacion, de advertencia y de consulta)
"""


from tkinter import *
from tkinter import messagebox

raiz = Tk()
raiz.title("Barra de Herramientas y Messagebox")

def infoAdicional():
    """
    Abre una ventana de informacion, cuando se ingresa a Barra de menu/Ayuda/Acerca de ..
    """
    messagebox.showinfo("Procesador de Santi", "Procesador version 1.0")

def avisoLicencia():
    """
    Abre una ventana de aviso, cuando se ingresa a Barra de menu/Ayuda/Licencia
    """
    messagebox.showwarning("Licencia", "Producto bajo licencia xxxxx")

def salirAplicacion():
    """
    Abre una ventana con una consulta, cuando se ingresa a Barra de menu/Archivo/Salir
    """
    # Opcion 1 con pregunta de Yes o No
    # respuesta = messagebox.askquestion("Salir", "¿Desesas salir de la aplicacióon?")

    # if respuesta == "yes":
    #     raiz.destroy()

    #Opcion 2 con pregunta de ok o cancel
    respuesta = messagebox.askokcancel("Salir", "¿Desesas salir de la aplicacióon?")

    if respuesta == True:
        raiz.destroy()

def cerraDocumento():
    respuesta=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")

    if respuesta == False:
        raiz.destroy()



#variable para el menu
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

#---------------------------------------------------------------------------------------------------
# ASIGNACION ELEMENTOS A LA BARRA DE MENU
archivoMenu = Menu(barraMenu, tearoff=0)
#tearoff es para sacar el "regloncito de guiones" (paracido al separator) que aparece cuando abris el menu
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerraDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas = Menu(barraMenu, tearoff=0)
archivoHerramientas.add_command(label="Herramienta 1")
archivoHerramientas.add_command(label="Herramienta 1")


archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de..", command=infoAdicional)



#---------------------------------------------------------------------------------------------------
# NOMBRES DE LOS ELEMENTOS DEL MENU
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


raiz.mainloop()