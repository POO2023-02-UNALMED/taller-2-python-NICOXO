class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        allowed_colors = ["rojo","verde","amarillo","negro","blanco"]
        if color in allowed_colors:
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        allowed_types = ["electrico","gasolina"]
        if tipo in allowed_types:
            self.tipo = tipo

class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, marca, registro,asientos,motor):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.registro = registro
        self.asientos = asientos
        self.motor = motor
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        return len([asiento for asiento in self.asiento if isinstance(asiento, Asiento)])
    
    def verificarIntegridad(self):
        registro = [self.registro]

        if self.motor:
            registro.append(self.motor.registro)

        for asiento in self.asientos:
            registro.append(asiento.registro)

        if len(set(registro)) == 1:
            return "Auto original"
        else:
            return "Las piezas no son originales"

