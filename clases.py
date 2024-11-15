from datetime import date, datetime

codigos_pedido = [] # para la clse Pedido 

class Fecha:
    def __init__(self, p_dia, p_mes, p_anio):
        if (
            isinstance(p_dia, int)
            and isinstance(p_mes, int)
            and isinstance(p_anio, int)
        ):
            if 0 < p_dia <= 31 and 0 < p_mes <= 12 and 1900 <= p_anio <= 2100:
                self.fecha = date(p_anio, p_mes, p_dia)
            else:
                raise AttributeError(
                    f"El día debe estar entre 1 - 31, el mes entre 1 - 12 y el año entre 1900 - 2100. Valores ingresados p_dia={p_dia} p_mes={p_mes} p_año={p_anio}"
                )
        else:
            raise AttributeError(
                f"Dia, Mes y Año deben ser del tipo int. Sin embargo son p_dia={type(p_dia)} p_mes={type(p_mes)} p_año={type(p_anio)}"
            )

    def __str__(self):
        return self.fecha.strftime("%d/%m/%y")

    def __eq__(self, other):
        if isinstance(other, Fecha):
            return self.fecha == other.fecha
        raise AttributeError(
            f"El parámetro other debe ser un objeto Fecha, en cambio se paso un objeto {type(other)}"
        )

    def __lt__(self, other):
        if isinstance(other, Fecha):
            return self.fecha < other.fecha
        raise AttributeError(
            f"El parámetro other debe ser un objeto Fecha, en cambio se paso un objeto {type(other)}"
        )

    def __le__(self, other):
        if isinstance(other, Fecha):
            return self.fecha <= other.fecha
        raise AttributeError(
            f"El parámetro other debe ser un objeto Fecha, en cambio se paso un objeto {type(other)}"
        )

    def __gt__(self, other):
        if isinstance(other, Fecha):
            return self.fecha > other.fecha
        raise AttributeError(
            f"El parámetro other debe ser un objeto Fecha, en cambio se paso un objeto {type(other)}"
        )

    def __ge__(self, other):
        if isinstance(other, Fecha):
            return self.fecha >= other.fecha
        raise AttributeError(
            f"El parámetro other debe ser un objeto Fecha, en cambio se paso un objeto {type(other)}"
        )

class Producto:
    codigos_ean = []  # aca guardamos los codigos ean usados y nuevos 

    def __init__(self, codigo_ean, nombre, precio):
        self.codigo_ean = codigo_ean
        self.nombre = nombre
        self.precio = float(precio)


# Clase Cliente
class Cliente:
    dnis_usados = []  

    def __init__(self, dni, nombre_apellido, fecha_nacimiento):
        dia, mes, anio = self.parse_fecha(fecha_nacimiento)
        if dia is None:
            print("Error: Fecha de nacimiento inválida. Debe estar en el formato 'DD/MM/AAAA'.")
            self.dni = None  
            return  

        self.dni = dni
        self.nombre_apellido = nombre_apellido
        self.fecha_nacimiento = f"{dia}/{mes}/{anio}"

        if self.dni in Cliente.dnis_usados:
            print(f"El DNI {self.dni} ya está registrado.")
            return

        Cliente.dnis_usados.append(self.dni)
        print("DNI del cliente agregado con éxito.")
        
    def parse_fecha(self, fecha_str):
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            return fecha.day, fecha.month, fecha.year
        except ValueError:
            return None, None, None 

    def __str__(self):
        return f"DNI: {self.dni}, Nombre: {self.nombre_apellido}, Fecha de Nacimiento: {self.fecha_nacimiento}"

    
# Clase Pedido
class Pedido:
    def __init__(
        self,
        codigo_identificador_de_pedido,
        productos,
        cliente,
        fecha_pedido,
        cargos_extra,
    ):
        if (
            codigo_identificador_de_pedido > 0
            and codigo_identificador_de_pedido not in codigos_pedido
        ):
            codigos_pedido.append(codigo_identificador_de_pedido)
            self.codigo_identificador_de_pedido = codigo_identificador_de_pedido
        else:
            raise ValueError(
                "El codigo de pedido debe ser un numero entero positivo y unico."
            )

        lista_valida = True
        for producto in productos:
            try:
                producto.codigo_ean
                producto.nombre
                producto.precio
            except AttributeError:
                lista_valida = False
                break
        if lista_valida:
            self.productos = productos
        else:
            raise ValueError(
                "La lista de productos debe contener solo objetos del tipo Producto."
            )

        try:
            cliente.dni
            cliente.nombre_apellido
            cliente.fecha_nacimiento
            self.cliente = cliente
        except AttributeError:
            raise ValueError(
                "El cliente debe ser un objeto valido con los atributos necesarios."
            )

        fecha_partes = fecha_pedido.split("/")
        if len(fecha_partes) != 3:
            raise ValueError(
                "La fecha de pedido debe estar en el formato 'DD/MM/AAAA'."
            )

        dia, mes, anio = fecha_partes
        if not (
            1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and 1900 <= int(anio) <= 2100
        ):
            raise ValueError(
                "La fecha de pedido debe estar en el formato 'DD/MM/AAAA' y ser valida."
            )

        self.fecha_pedido = fecha_pedido

        try:
            self.cargos_extra = float(cargos_extra)
        except ValueError:
            raise ValueError("Los cargos extra deben ser un numero decimal (flotante).")

    def parse_fecha(self, fecha_str):
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            return fecha.day, fecha.month, fecha.year
        except ValueError:
            return None, None, None

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio

        if self.cargos_extra < 0:
            descuento = total * (self.cargos_extra / 100)
            total += descuento  
        else:
            recargo = total * (self.cargos_extra / 100)
            total += recargo  
        return total