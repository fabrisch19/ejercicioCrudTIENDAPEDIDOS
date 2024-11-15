from clases import Producto, Cliente, Pedido, Fecha 
from gestion import *
import manejo_archivos_binarios
guardar_datos_en_archivo = manejo_archivos_binarios.guardar_datos_en_archivo
cargar_datos_desde_archivo = manejo_archivos_binarios.cargar_datos_desde_archivo

def main():
    while True:
        print("BIENVENIDO A LA TIENDA UNPAZ - LGTI")
        print("Menu Principal:")
        print("1. Gestion de Clientes")
        print("2. Gestion de Productos")
        print("3. Gestion de Pedidos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            menu_clientes()
        elif opcion == '2':
            menu_productos()
        elif opcion == '3':
            menu_pedidos()
        elif opcion == '4':
            print("Chau nos vemos, espero que este programa te haya funcionado")
            break
        else:
            print("Opcion incorrecta, intenta de nuevo.")

def menu_clientes():
    clientes = cargar_datos_desde_archivo("clientes.bin")
    if not clientes:
        clientes = []

    # inicializamos la lista de dnis 
    Cliente.dnis_usados = [cliente.dni for cliente in clientes]

    while True:
        print("Gestion de Clientes:")
        print("1. Crear un nuevo cliente")
        print("2. Consultar todos los clientes")
        print("3. Consultar cliente por dni")
        print("4. Actualizar un cliente")
        print("5. Eliminar un cliente")
        print("6. Volver al menu principal")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            crear_cliente(clientes)
        elif opcion == "2":
            consultar_clientes(clientes)
        elif opcion == "3":
            consultar_cliente_por_dni(clientes)
        elif opcion == "4":
            actualizar_cliente(clientes)
        elif opcion == "5":
            eliminar_cliente(clientes)
        elif opcion == "6":
            guardar_datos_en_archivo("clientes.bin", clientes)
            break
        else:
            print("Opcion no valida, intente nuevamente.")

def menu_productos():
    productos = cargar_datos_desde_archivo("productos.bin")
    if not productos:
        productos = []

    Producto.codigos_ean = []
    for prod in productos:
        Producto.codigos_ean.append(prod.codigo_ean)

    while True:
        print("Gestion de Productos:")
        print("1. Crear un nuevo producto")
        print("2. Consultar todos los productos")
        print("3. Consultar producto por codigo EAN")
        print("4. Actualizar un producto")
        print("5. Eliminar un producto")
        print("6. Volver al menu principal")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            crear_producto(productos)
        elif opcion == "2":
            consultar_productos(productos)
        elif opcion == "3":
            consultar_producto_por_codigo_ean(productos)
        elif opcion == "4":
            actualizar_producto(productos)
        elif opcion == "5":
            eliminar_producto(productos)
        elif opcion == "6":
            guardar_datos_en_archivo("productos.bin", productos)
            break
        else:
            print("Opcion no valida, intente nuevamente.")

def menu_pedidos():
    pedidos = cargar_datos_desde_archivo("pedidos.bin")
    productos = cargar_datos_desde_archivo("productos.bin")
    clientes = cargar_datos_desde_archivo("clientes.bin")
    while True:
        print("Gestion de Pedidos:")
        print("1. Crear un nuevo pedido")
        print("2. Consultar pedidos por codigo")
        print("3. Consultar todos los pedidos realizados")
        print("4. Actualizar un pedido")
        print("5. Eliminar un pedido")
        print("6. Ordenar pedidos por importe total")
        print("7. Volver al menu principal")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            crear_pedido(pedidos, productos, clientes)
        elif opcion == "2":
            consultar_pedidos_por_codigo_identificador(pedidos)
        elif opcion == "3":
            consultar_todos_los_pedidos(pedidos)
        elif opcion == "4":
            actualizar_pedido(pedidos, productos)
        elif opcion == "5":
            eliminar_pedido(pedidos)
        elif opcion == "6":
            ordenar_pedidos_por_total(pedidos)
            consultar_todos_los_pedidos(pedidos)
        elif opcion == "7":
            guardar_datos_en_archivo("pedidos.bin", pedidos)
            break
        else:
            print("Opcion no valida, intente nuevamente.")

if __name__ == '__main__':
    main()

