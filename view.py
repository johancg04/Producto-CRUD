import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from datetime import date
from controller import *
from entity import *
from tkinter import PhotoImage

i_con_tilde = 'i' + u'\u0301'
o_con_tilde = 'o' + u'\u0301'

categoria_texto = 'Categor' + i_con_tilde + 'a'
codigo_texto = 'C' + o_con_tilde + 'digo'


class Application:
    # constructor
    def __init__(self):
        self.ventana = tk.Tk()
        self.obj = ProductoController()
        # Variables de la clase
        self.vCodigo = tk.StringVar()
        self.vNombre = tk.StringVar()
        self.vCategoria = tk.StringVar()
        self.vPrecio = tk.StringVar()
        self.vCantidad = tk.StringVar()
        self.vfecha = tk.StringVar()

        self.vfecha.set(date.today().strftime("%d/%m/%Y"))

        # VENTANAS
        self.ventana.title(":: CRUD DE PRODUCTOS ::")
        self.ventana.geometry("540x580")
        self.ventana.configure(background="Cyan")

        # TITULO
        self.Label1 = tk.Label(text="CRUD DE PRODUCTOS", bg="Cyan", fg="red", font=(
            "Arial", 16, "bold")).place(x=120, y=10)
        # ETIQUETAS
        self.label2 = tk.Label(text=codigo_texto, bg="Cyan",
                               fg="red").place(x=50, y=50)
        self.txtbox1 = tk.Entry(
            self.ventana, textvariable=self.vCodigo, width=10).place(x=175, y=50)

        self.label3 = tk.Label(text="Nombre", bg="Cyan",
                               fg="red").place(x=50, y=80)
        self.txtbox2 = tk.Entry(textvariable=self.vNombre,
                                width=30).place(x=175, y=80)

        self.label4 = tk.Label(text=categoria_texto, bg="Cyan",
                               fg="red").place(x=50, y=110)
        self.txtbox3 = tk.Entry(textvariable=self.vCategoria,
                                width=10).place(x=175, y=110)

        self.label5 = tk.Label(text="Precio", bg="Cyan",
                               fg="red").place(x=50, y=140)
        self.txtbox4 = tk.Entry(textvariable=self.vPrecio,
                                width=10).place(x=175, y=140)

        self.label6 = tk.Label(text="Cantidad", bg="Cyan",
                               fg="red").place(x=50, y=170)
        self.txtbox5 = tk.Entry(textvariable=self.vCantidad,
                                width=10).place(x=175, y=170)

        self.label7 = tk.Label(text="Fecha", bg="Cyan",
                               fg="red").place(x=50, y=200)
        self.txtbox6 = tk.Entry(textvariable=self.vfecha,
                                state="disable", width=10).place(x=175, y=200)
        # BOTONES
        photo = PhotoImage(file="save_all.png")

        self.btn6 = tk.Button(image=photo, command=self.buscar,
                              width=40, height=30).place(x=260, y=40)
        self.btn1 = tk.Button(
            text="Grabar", command=self.insertardatos, width=8).place(x=40, y=230)

        self.btn2 = tk.Button(
            text="Modificar", command=self.actualizardatos, width=8).place(x=110, y=230)

        self.btn3 = tk.Button(
            text="Eliminar", command=self.eliminar, width=8).place(x=190, y=230)

        self.btn4 = tk.Button(
            text="Listar", command=self.listardatos, width=8).place(x=260, y=230)

        self.btn5 = tk.Button(
            text="Limpiar", command=self.nuevo, width=8).place(x=320, y=230)

        # frame
        self.tree_frame = tk.Frame(self.ventana)
        self.tree_frame.config(height=5)
        self.tree_frame.pack(side=BOTTOM)
        # TABLA
        self.tv = ttk.Treeview(self.tree_frame, selectmode='browse')
        self.tv['columns'] = ('Codigo', 'Nombre',
                              'Categoria', 'Precio', 'Cantidad')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('Codigo', anchor=CENTER, width=60, minwidth=60)
        self.tv.column('Nombre', anchor=tk.W, width=120, minwidth=120)
        self.tv.column('Categoria', anchor=tk.W, width=120, minwidth=120)
        self.tv.column('Precio', anchor=tk.E, width=110, minwidth=110)
        self.tv.column('Cantidad', anchor=tk.E, width=110, minwidth=110)
        vsb = ttk.Scrollbar(
            self.tree_frame, orient="vertical", command=self.tv.yview)
        vsb.pack(side='right', fill='y')
        self.tv.configure(yscrollcommand=vsb.set)

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('Codigo', text='Id', anchor=CENTER)
        self.tv.heading('Nombre', text='Nombre', anchor=CENTER)
        self.tv.heading('Categoria', text=categoria_texto, anchor=CENTER)
        self.tv.heading('Precio', text='Precio', anchor=CENTER)
        self.tv.heading('Cantidad', text='Cantidad', anchor=CENTER)
        self.tv.pack(side=BOTTOM)
        self.listardatos()
        self.ventana.mainloop()

    def insertardatos(self):
        print('Valor Precio:', self.vPrecio.get())
        produ = Producto(self.vCodigo.get(), self.vNombre.get(
        ), self.vCategoria.get(), float(self.vPrecio.get()), int(self.vCantidad.get()))
        msg = self.obj.procesarProducto(produ, 1)
        tkinter.messagebox.showinfo("Informacion", msg)
        self.nuevo()
        self.listardatos()

    def listardatos(self):
        for i in self.tv.get_children():
            self.tv.delete(i)
        productos = self.obj.listaProductos()
        for p in productos:
            self.tv.insert('', 'end', values=(
                p['codigo'], p['nombre'], p['categoria'], p['precio'], p['cantidad']))

    def actualizardatos(self):
        produ = Producto(self.vCodigo.get(), self.vNombre.get(
        ), self.vCategoria.get(), str(self.vPrecio.get()), str(self.vCantidad.get()))
        msg = self.obj.procesarProducto(produ, 2)
        tkinter.messagebox.showinfo("Informacion", msg)
        self.nuevo()
        self.listardatos()

    def nuevo(self):
        self.vCodigo.set("")
        self.vNombre.set("")
        self.vCategoria.set("")
        self.vPrecio.set("")
        self.vCantidad.set("")
        for i in self.tv.get_children():
            self.tv.delete(i)

    def eliminar(self):
        produ = Producto(self.vCodigo.get(), self.vNombre.get(
        ), self.vCategoria.get(), str(self.vPrecio.get()), str(self.vCantidad.get()))
        msg = self.obj.procesarProducto(produ, 3)
        tkinter.messagebox.showinfo("Informacion", msg)
        self.nuevo()
        self.listardatos()

    def buscar(self):
        codigo = self.vCodigo.get()
        Producto = self.obj.buscarProducto(codigo)
        if Producto != None:
            self.vCodigo.set(Producto[0])
            self.vNombre.set(Producto[1])
            self.vCategoria.set(Producto[2])
            self.vPrecio.set(Producto[3])
            self.vCantidad.set(Producto[4])
        else:
            tkinter.messagebox.showwarning("Aviso", "Producto no existe")
            self.nuevo()


x = Application()
