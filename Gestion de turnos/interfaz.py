import tkinter as tk
from tkinter import messagebox


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertarFinal(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
            return

        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo

    def mostrar(self):
        datos = []
        actual = self.cabeza
        while actual:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if valor.lower() in actual.dato.lower():
                return True
            actual = actual.siguiente
        return False


lista = ListaEnlazada()


def agregar_turno():
    nombre = entrada_nombre.get()
    servicio = entrada_servicio.get()
    hora = entrada_hora.get()

    if nombre == "" or servicio == "" or hora == "":
        messagebox.showwarning("Error", "Complete todos los campos")
        return

    dato = nombre + " - " + servicio + " - " + hora
    lista.insertarFinal(dato)

    messagebox.showinfo("Correcto", "Turno agregado")

    entrada_nombre.delete(0, tk.END)
    entrada_servicio.delete(0, tk.END)
    entrada_hora.delete(0, tk.END)


def mostrar_turnos():
    area_texto.delete("1.0", tk.END)

    turnos = lista.mostrar()

    if len(turnos) == 0:
        area_texto.insert(tk.END, "No hay turnos\n")
    else:
        for t in turnos:
            area_texto.insert(tk.END, t + "\n")


def buscar_turno():
    nombre = entrada_buscar.get()

    if lista.buscar(nombre):
        messagebox.showinfo("Resultado", "Turno encontrado")
    else:
        messagebox.showerror("Resultado", "No existe ese turno")


ventana = tk.Tk()
ventana.title("Sistema de Turnos - Peluquería")
ventana.geometry("450x500")


titulo = tk.Label(ventana, text="Gestión de Turnos", font=("Arial", 16))
titulo.pack(pady=10)


tk.Label(ventana, text="Nombre").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(ventana, text="Servicio").pack()
entrada_servicio = tk.Entry(ventana)
entrada_servicio.pack()

tk.Label(ventana, text="Hora").pack()
entrada_hora = tk.Entry(ventana)
entrada_hora.pack()


boton_agregar = tk.Button(ventana, text="Agregar Turno", command=agregar_turno)
boton_agregar.pack(pady=10)


boton_mostrar = tk.Button(ventana, text="Mostrar Turnos", command=mostrar_turnos)
boton_mostrar.pack(pady=5)


tk.Label(ventana, text="Buscar por nombre").pack()
entrada_buscar = tk.Entry(ventana)
entrada_buscar.pack()


boton_buscar = tk.Button(ventana, text="Buscar Turno", command=buscar_turno)
boton_buscar.pack(pady=10)


area_texto = tk.Text(ventana, height=10, width=40)
area_texto.pack(pady=10)


ventana.mainloop()