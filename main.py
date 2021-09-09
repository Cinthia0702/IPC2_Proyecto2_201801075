# Cinthia Quiñonez
# 201801075

from os import startfile, system, write
from xml.dom import minidom
from tkinter import* 
import tkinter as tk
from tkinter import Image
from tkinter.filedialog import askopenfilename

def cargar_archivo_maquina():
    ruta=Tk()
    ruta.withdraw()
    ruta.update()
    try:
        archivoMaquina=askopenfilename(filetypes=[("Text files", "*.xml")])
        archivo=open(archivoMaquina,mode='r')
        archivo_cargado=minidom.parse(archivo)
        print('\nArchivo Máquina')
        CLProduccion=archivo_cargado.getElementsByTagName('CantidadLineasProduccion')
        print('\nCantidad de Producciones: ',CLProduccion.length)
        for hijo in CLProduccion:
            print('Cantidad de lineas de producción: ',hijo.firstChild.data)
        for hijo in archivo_cargado.getElementsByTagName('ListadoLineasProduccion'):
            for subHijo in hijo.getElementsByTagName('LineaProduccion'):
                print('--------------------------------------------------')
                for subSubHijo in subHijo.getElementsByTagName('Numero'):
                    print('Número: ',subSubHijo.firstChild.data)
                for subSubHijo in subHijo.getElementsByTagName('CantidadComponente'):
                    print('Cantidad de componentes: ',subSubHijo.firstChild.data)
                for subSubHijo in subHijo.getElementsByTagName('TiempoEnsamblaje'):
                    print('Tiempo: ',subSubHijo.firstChild.data)
        for hijo in archivo_cargado.getElementsByTagName('ListadoProductos'):
            for subHijo in hijo.getElementsByTagName('Producto'):
                print('--------------------------------------------------')
                for subSubHijo in subHijo.getElementsByTagName('nombre'):
                    print('Nombre: ',subSubHijo.firstChild.data)
                for subSubHijo in subHijo.getElementsByTagName('elaboracion'):
                    print(subSubHijo.firstChild.data)
    except:
        print('No se puede abrir el archivo')

def cargar_archivo_simulacion():
    ruta=Tk()
    ruta.withdraw()
    ruta.update()
    try:
        archivoMaquina=askopenfilename(filetypes=[("Text files", "*.xml")])
        archivo=open(archivoMaquina,mode='r')
        archivo_cargado=minidom.parse(archivo)
        print('\nArchivo Simulación')
        nombre=archivo_cargado.getElementsByTagName('Nombre')
        print('\nCantidad: ',nombre.length)
        for hijo in nombre:
            print('Nombre: ',hijo.firstChild.data)
        for hijo in archivo_cargado.getElementsByTagName('ListadoProductos'):
            for subHijo in hijo.getElementsByTagName('Producto'):
                print('Producto: ',subHijo.firstChild.data)
    except:
        print('No se puede abrir el archivo')

def reporte_html():
    pass

def reporte_graphviz():
    pass

ventana=Tk()
ventana.title('Principal')
ventana.geometry("1250x650")
ventana.iconbitmap("icono.ico")
ventana.config(bg="#7eb8da")
ventana.resizable(0,0)

menu_opciones=Menu(ventana)
ventana.config(menu=menu_opciones)
cargar_archivo=Menu(menu_opciones)
reporte=Menu(menu_opciones)
ayuda=Menu(menu_opciones)

cargar_archivo.add_command(label="Cargar archivo Maquina",font=("Consolas",12),command=cargar_archivo_maquina)
cargar_archivo.add_command(label="Cargar archivo producto",font=("Consolas",12),command=cargar_archivo_simulacion)
reporte.add_command(label="Reporte HTML",font=("Consolas",12),command=reporte_html)
reporte.add_command(label="Reporte Graphviz",font=("Consolas",12),command=reporte_graphviz)

menu_opciones.add_cascade(label="Cargar Archivo",menu=cargar_archivo)
menu_opciones.add_cascade(label="Reportes",menu=reporte)
menu_opciones.add_cascade(label="Ayuda")

ventana.config(menu=menu_opciones)

label_info=Label(ventana,height=1,width=20,bg="#7eb8da",text="Nombre del producto",font=("Consolas",20))
label_info.place(x=50,y=100)

img_robot=PhotoImage(file="robot.png")
reduccion_img_robot=img_robot.subsample(3)
label_robot=Label(ventana,height=250,width=200,image=reduccion_img_robot)
label_robot.place(x=100,y=150)

img_siguiente=PhotoImage(file="siguiente.png")
reduccion_img_siguiente=img_siguiente.subsample(5)
button_next=Button(ventana,height=75,width=75,image=reduccion_img_siguiente)
button_next.place(x=1100,y=400)

img_ensamblar=PhotoImage(file="ensamblar.png")
reduccion_img_ensamblar=img_ensamblar.subsample(12)
button_join=Button(ventana,height=75,width=75,image=reduccion_img_ensamblar)
button_join.place(x=1000,y=400)

img_anterior=PhotoImage(file="anterior.png")
reduccion_img_anterior=img_anterior.subsample(4)
button_before=Button(ventana,height=75,width=75,image=reduccion_img_anterior)
button_before.place(x=900,y=400)

ventana.mainloop()