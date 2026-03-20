class Nodo:
    def __init__(self, nombre, servicio, hora):
        self.nombre = nombre
        self.servicio = servicio
        self.hora = hora
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertarFinal(self, nombre, servicio, hora):
        nuevo = Nodo(nombre, servicio, hora)

        if self.cabeza is None:
            self.cabeza = nuevo
            return

        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo

    def mostrar(self):
        if self.cabeza is None:
            print("No hay turnos")
            return

        actual = self.cabeza
        while actual:
            print(actual.nombre, "-", actual.servicio, "-", actual.hora)
            actual = actual.siguiente

    def buscar(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre.lower() == nombre.lower():
                print("Turno encontrado:", actual.nombre, actual.servicio, actual.hora)
                return True
            actual = actual.siguiente
        print("No existe ese turno")
        return False

    def atender(self):
        if self.cabeza is None:
            print("No hay clientas")
            return

        atendida = self.cabeza
        self.cabeza = self.cabeza.siguiente
        print("Atendiendo a", atendida.nombre)

    def cancelar(self, nombre):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.nombre.lower() == nombre.lower():
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                print("Turno cancelado")
                return

            anterior = actual
            actual = actual.siguiente

        print("No se encontró el turno")


turnos = ListaEnlazada()

while True:

    print("\nSistema de Turnos Peluquería")
    print("1 Registrar turno")
    print("2 Mostrar turnos")
    print("3 Buscar turno")
    print("4 Atender clienta")
    print("5 Cancelar turno")
    print("6 Salir")

    op = input("Opción: ")

    if op == "1":
        nombre = input("Nombre: ")
        servicio = input("Servicio: ")
        hora = input("Hora: ")
        turnos.insertarFinal(nombre, servicio, hora)

    elif op == "2":
        turnos.mostrar()

    elif op == "3":
        nombre = input("Nombre a buscar: ")
        turnos.buscar(nombre)

    elif op == "4":
        turnos.atender()

    elif op == "5":
        nombre = input("Nombre a cancelar: ")
        turnos.cancelar(nombre)

    elif op == "6":
        break

    else:
        print("Opción inválida")