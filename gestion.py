from clases import Producto, Cliente, Pedido, Fecha

def crear_producto(productos):
    while True:
        # se valida codigo ean
        while True:
            try:
                codigo_ean = input("Ingresa el codigo EAN del producto: ")
                if codigo_ean == '':
                    raise ValueError("El codigo EAN no puede estar vacio.")
                codigo_ean = int(codigo_ean)  # se lo pasa a tipo entero
                if codigo_ean < 0:
                    print("El codigo EAN no puede ser negativo. Intenta de nuevo.")
                    continue
                if codigo_ean in Producto.codigos_ean:
                    print(f"El codigo EAN {codigo_ean} ya esta siendo usado, proba con otro.")
                    continue
                break  # listo codigo ean valido pasa
            except ValueError as s:
                print(f"Error: {s}. Ingresa un numero entero para el codigo EAN.")
        
        # validamos nom produc
        while True:
            nombre = input("Ingresa el nombre del producto: ")
            if not nombre:  # se verifica que no este vacio
                print("El nombre no puede estar vacio. Intenta de nuevo.")
            elif len(nombre) > 50:  # si se pasa de 50 caracteres chau
                print("El nombre no puede tener mas de 50 caracteres. Intenta de nuevo.")
            else:
                break  # listo nombre valido
        
        # validamos precio
        while True:
            try:
                precio = float(input("Ingresa el precio del producto: "))
                if precio < 0:
                    print("El precio no puede ser negativo. Intenta de nuevo.")
                else:
                    break  # liisto precioo valido
            except ValueError:
                print("El precio tiene que ser un numero valido. Intenta de nuevo.")

        # creamos producto, validamos el codigo ean y el precio
        producto = Producto(codigo_ean, nombre, precio)

        # se comprueba los codigos y el nombre
        if codigo_ean in Producto.codigos_ean:
            print("No se pudo crear el producto porque el codigo EAN esta repetido.")
        elif len(nombre) > 50:
            print("No se pudo crear el producto porque el nombre tiene mas de 50 caracteres.")
        else:
            # listo procedemos a crear el producto
            productos.append(producto)
            Producto.codigos_ean.append(codigo_ean)  # se lo agrega a codigos ean los codigos usados
            print("Producto creado con exito.")
        
        while True:
            agregar_otro = input("¿Querés agregar otro producto? (s/n): ").lower()
            if agregar_otro == "s":
                break  
            elif agregar_otro == "n":
                print("Operacion terminada.")
                return  
            else:
                print("Por favor, ingresa 's' o 'n'.")

def consultar_productos(productos):
    if not productos:
        print("No hay productos registrados.")
        return

    ordenar_productos_por_codigo_ean(productos)

    print("Productos ordenados de menor a mayor por codigo_ean")
    for producto in productos:
        print(
            f"Codigo EAN: {producto.codigo_ean}, Nombre: {producto.nombre}, Precio: ${producto.precio}"
        )

def buscar_producto_por_codigo_identificador(codigo_identificador, productos):
    """
    Busqueda binaria para productos.
        Precondicion: lista de productos ordenada por codigo EAN.
        Devuelve None si no existe un producto con ese codigo.
        Devuelve la instancia del producto cuyo codigo coincide.
    """
    izq = 0
    der = len(productos) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if productos[medio].codigo_ean == codigo_identificador:
            return productos[medio]
        elif productos[medio].codigo_ean > codigo_identificador:
            der = medio - 1
        else:
            izq = medio + 1
    return None

def consultar_producto_por_codigo_ean(productos):
    """
    Permite al usuario consultar productos por su codigo EAN utilizando busqueda binaria.
    """
    while True:
        while True:
            codigo_ean = input("Ingresa el codigo EAN del producto a consultar: ")
            if not codigo_ean.isdigit():
                print("Debes ingresar un numero valido.")
                continue  # volvemos a pedir el codigo si no es valido
            
            codigo_ean = int(codigo_ean)
            producto = buscar_producto_por_codigo_identificador(codigo_ean, productos)

            if producto:
                print(f"Producto encontrado:")
                print(f"Codigo EAN: {producto.codigo_ean}, Nombre: {producto.nombre}, Precio: ${producto.precio}")
            else:
                print(f"No se encontro un producto con el codigo EAN: {codigo_ean}")

            while True:
                continuar = input("¿Deseas buscar otro producto por codigo EAN? (s/n): ").lower()
                if continuar == "s":
                    break
                elif continuar == "n":
                    print("Operacion terminada.")
                    return
                else:
                    print("Por favor, ingresa 's' o 'n'.")

def actualizar_producto(productos):
    while True:
        while True:
            codigo_ean = input("Ingresa el codigo EAN del producto a actualizar: ")
            if not codigo_ean.isdigit() or int(codigo_ean) < 0:
                print("Debes ingresar un numero valido y positivo.")
                continue  # volvemos a pedir el codigo si no es valido
            codigo_ean = int(codigo_ean)
            break

        # Verificamos si el producto existe
        producto = buscar_producto_por_codigo_identificador(codigo_ean, productos)
        
        if producto:
            # actualizar nombre producto
            while True:
                nuevo_nombre = input(f"Ingrese el nuevo nombre del producto (actual: {producto.nombre}): ")
                if len(nuevo_nombre) > 50:
                    print("El nombre del producto no puede tener mas de 50 caracteres. Intente de nuevo.")
                elif nuevo_nombre == "":
                    print("El nombre del producto no ha sido modificado. Se mantiene el nombre actual.")
                    break  # mantiene el nombre actual
                else:
                    producto.nombre = nuevo_nombre
                    break  # se actualiza el nombre

            # actualizar precio
            while True:
                nuevo_precio = input(f"Ingrese el nuevo precio del producto (actual: ${producto.precio}): ")
                if nuevo_precio:
                    try:
                        nuevo_precio = float(nuevo_precio)
                        if nuevo_precio < 0:
                            print("El precio no puede ser negativo. Intente de nuevo.")
                        else:
                            producto.precio = nuevo_precio
                            break
                    except ValueError:
                        print("Debe ingresar un valor numerico. Intente de nuevo.")
                else:
                    break  # no se modifica el precio si esta vacio

            # actualizar codigo ean
            while True:
                nuevo_codigo_ean = input(f"Ingrese el nuevo codigo EAN del producto (actual: {producto.codigo_ean}): ")
                if nuevo_codigo_ean == "":
                    print("No se actualizo el codigo EAN. El producto mantiene su codigo actual.")
                    break

                # Verificar si el nuevo codigo EAN es positivo y unico
                if not nuevo_codigo_ean.isdigit() or int(nuevo_codigo_ean) < 0:
                    print("El codigo EAN debe ser un numero positivo.")
                    continue
                
                nuevo_codigo_ean = int(nuevo_codigo_ean)
                ean_duplicado = False
                for p in productos:
                    if p.codigo_ean == nuevo_codigo_ean:
                        ean_duplicado = True
                        break

                if ean_duplicado:
                    print(f"Error: El codigo EAN {nuevo_codigo_ean} ya esta en uso. Debe ser unico.")
                    while True:
                        continuar = input("¿Desea ingresar otro codigo EAN? (s/n): ").lower()
                        if continuar == "s":
                            break  # permite intentar ingresar otro codigo EAN
                        elif continuar == "n":
                            print("Operacion cancelada.")
                            return  
                        else:
                            print("Por favor, ingrese 's' o 'n'.")
                else:
                    producto.codigo_ean = nuevo_codigo_ean
                    print("Codigo EAN actualizado con exito.")
                    break

            print("Producto actualizado con exito.")
        else:
            print("Producto no encontrado. Intente nuevamente.")

        while True:
            continuar = input("¿Desea actualizar otro producto? (s/n): ").lower()
            if continuar == "s":
                break  
            elif continuar == "n":
                print("Operacion terminada.")
                return  
            else:
                print("Por favor, ingrese 's' o 'n'.")

def eliminar_producto(productos):
    while True:
        ordenar_productos_por_codigo_ean(productos)
        
        # solicitamos el codigo y que ademas validemos este dato 
        while True:
            codigo_ean = input("Ingresa el codigo EAN del producto a eliminar: ")
            if not codigo_ean.isdigit():
                print("Debes ingresar un numero valido.")
                continue  # volvemos a pedir el codigo si no es valido
            codigo_ean = int(codigo_ean)
            break

        producto = buscar_producto_por_codigo_identificador(codigo_ean, productos)

        if producto:
            while True:
                confirmacion = input(
                    f"¿Estas seguro de eliminar el producto {producto.nombre}? (s/n): "
                ).lower()

                if confirmacion == "s":
                    productos.remove(producto)
                    print("Producto eliminado con exito.")
                    break  
                elif confirmacion == "n":
                    print("Eliminacion cancelada.")
                    break  
                else:
                    print("Por favor, ingrese 's' o 'n'.")

            while True:
                eliminar_otro = input("¿Deseas eliminar otro producto? (s/n): ").lower()
                if eliminar_otro == "s":
                    break  
                elif eliminar_otro == "n":
                    print("Operacion terminada.")
                    return 
                else:
                    print("Por favor, ingrese 's' o 'n'.")

        else:
            print("Producto no encontrado. Intente nuevamente.")

def mezclar_por_codigo_ean(lista, inicio, medio, fin):
    izquierda = lista[inicio : medio + 1]
    derecha = lista[medio + 1 : fin + 1]

    i = j = 0
    k = inicio

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i].codigo_ean <= derecha[j].codigo_ean:
            lista[k] = izquierda[i]
            i += 1
        else:
            lista[k] = derecha[j]
            j += 1
        k += 1

    while i < len(izquierda):
        lista[k] = izquierda[i]
        i += 1
        k += 1

    while j < len(derecha):
        lista[k] = derecha[j]
        j += 1
        k += 1

def merge_sort_por_codigo_ean(lista, inicio, fin):

    if inicio < fin:
        medio = (inicio + fin) // 2

        merge_sort_por_codigo_ean(lista, inicio, medio)

        merge_sort_por_codigo_ean(lista, medio + 1, fin)

        mezclar_por_codigo_ean(lista, inicio, medio, fin)


def ordenar_productos_por_codigo_ean(productos):
    merge_sort_por_codigo_ean(productos, 0, len(productos) - 1)

#FUNCIONES CLIENTE
def crear_cliente(clientes):
    while True:
        try:
            dni = int(input("Ingresa el DNI del cliente a crear: "))
            
            if dni < 0:
                print("El DNI no puede ser negativo. Por favor, ingresa un numero valido.")
                continue
            
            if dni in Cliente.dnis_usados:
                while True:
                    continuar = input(f"El DNI {dni} ya esta en nuestro sistema. ¿Deseas intentar con otro? (s/n): ").lower()
                    if continuar == "s":
                        break
                    elif continuar == "n":
                        print("Operacion terminada.")
                        return
                    else:
                        print("Por favor, ingresa 's' o 'n'.")
                continue

        except ValueError:
            print("Debes ingresar un dato numerico para el DNI.")
            continue

        while True:
            nombre_apellido = input("Ingresa el nombre y apellido del cliente: ")
            if nombre_apellido != "":
                if len(nombre_apellido) > 60:
                    print("El nombre y apellido no puede tener mas de 60 caracteres. Intenta de nuevo.")
                else:
                    break
            else:
                print("El nombre y apellido no puede estar vacio, aunque sea agrega algo.")

        while True:
            fecha_nacimiento = input("Ingresa la fecha de nacimiento (DD/MM/AAAA): ")
            cliente = Cliente(dni, nombre_apellido, fecha_nacimiento)
            if cliente.dni is not None:
                break
            else:
                print("Por favor, ingresa una fecha valida en el formato 'DD/MM/AAAA'.")

        clientes.append(cliente)
        print("Cliente creado con exito.")

        while True:
            agregar_otro = input("¿Deseas agregar otro cliente? (s/n): ").lower()
            if agregar_otro == "s":
                break
            elif agregar_otro == "n":
                print("Operacion terminada.")
                return
            else:
                print("Por favor, ingresa 's' o 'n'.")

def consultar_clientes(clientes):
    if not clientes:
        print("No hay clientes registrados.")
        return

    ordenar_clientes_por_dni(clientes)

    for cliente in clientes:
        print(cliente)

def consultar_cliente_por_dni(clientes):
    while True:
        # aca solicitamos el dni hasta que sea valido tambien 
        while True:
            dni_input = input("Ingrese el DNI del cliente a consultar: ")
            if dni_input.isdigit():  # primero vemos que sea numero de tipo digito 
                dni = int(dni_input)
                break  # listo nos vamos del bucle si es valido 
            else:
                print("Debe ingresar un numero valido para el DNI.")

        cliente = buscar_cliente_por_codigo_dni(dni, clientes)

        if cliente:
            print("Cliente encontrado:")
            print(cliente)
        else:
            print(f"No se encontro un cliente con el DNI {dni}.")
      
        while True:
            continuar = input("¿Desea consultar otro cliente? (s/n): ").lower()
            if continuar == "s":
                break  
            elif continuar == "n":
                print("Operacion terminada.")
                return  
            else:
                print("Por favor, ingrese 's' o 'n'.")

def buscar_cliente_por_codigo_dni(dni, clientes):
    """
    Busqueda binaria para clientes.
        Precondicióo: lista de clientes ordenada por DNI.
        Devuelve None si no existe un cliente con ese DNI.
        Devuelve la instancia del cliente cuyo DNI coincide.
    """
    izq = 0
    der = len(clientes) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if clientes[medio].dni == dni:
            return clientes[medio]
        elif clientes[medio].dni > dni:
            der = medio - 1
        else:
            izq = medio + 1
    return None

def actualizar_cliente(clientes):
    while True:
        # validamos dni
        while True:
            dni_input = input("Ingrese el DNI del cliente a actualizar: ")
            if dni_input.isdigit():  # primero vemos que sea numero
                dni = int(dni_input)
                break  # listo nos vemos, es valido
            else:
                print("Debe ingresar un numero valido para el DNI.")

        #buscar cliente por dni
        cliente = buscar_cliente_por_codigo_dni(dni, clientes)

        if cliente:
            # actualizamos nombre y apellido
            while True:
                nuevo_nombre = input(f"Ingrese el nuevo nombre y apellido del cliente (actual: {cliente.nombre_apellido}): ")
                if len(nuevo_nombre) > 60:
                    print("El nombre y apellido no puede tener más de 60 caracteres. Intente de nuevo.")
                elif nuevo_nombre == "":
                    print("El nombre y apellido no ha sido modificado. El cliente mantiene su nombre actual.")
                    break  # mantiene el nombre actual
                else:
                    cliente.nombre_apellido = nuevo_nombre
                    break  # se actualiza el nombre

            # actualizamos la fecha
            while True:
                nuevo_fecha_nacimiento = input(f"Ingrese la nueva fecha de nacimiento (DD/MM/AAAA, actual: {cliente.fecha_nacimiento}): ")
                if nuevo_fecha_nacimiento == "":  #si no se ingresa se mantiene la fecha actual
                    print("La fecha de nacimiento no ha sido modificada.")
                    break  # si no la quiere modificar nos salimos del bucle
                else:
                    dia, mes, anio = Cliente.parse_fecha(cliente, nuevo_fecha_nacimiento)
                    if dia is not None:
                        cliente.fecha_nacimiento = f"{dia}/{mes}/{anio}"
                        break  # listo la fecha es valida, sali del bucle
                    else:
                        print("Fecha invalida. Asegura de ingresar el formato 'DD/MM/AAAA'.")

            # actualizamos dni
            while True:
                nuevo_dni = input(f"Ingrese el nuevo DNI del cliente (actual: {cliente.dni}): ")
                if nuevo_dni == "":  # si no se ingresa el dni mantenmos el actual
                    print("No se actualizó el DNI. El cliente continúa con su DNI actual.")
                    break

                if nuevo_dni.isdigit() and int(nuevo_dni) in Cliente.dnis_usados and int(nuevo_dni) != cliente.dni:
                    print(f"Error: El DNI {nuevo_dni} ya ha sido utilizado. Debe ser único.")
                    while True:
                        continuar = input("¿Desea ingresar otro DNI? (s/n): ").lower()
                        if continuar == "s":
                            break
                        elif continuar == "n":
                            break
                        else:
                            print("Por favor, ingrese 's' o 'n'.")

                    if continuar != "s":
                        break
                else:
                    if int(nuevo_dni) != cliente.dni:
                        Cliente.dnis_usados.remove(cliente.dni)
                    cliente.dni = int(nuevo_dni)
                    Cliente.dnis_usados.append(cliente.dni)
                    print("DNI actualizado con exito.")
                    break

            print("Cliente actualizado con exito.")
        else:
            print("Cliente no encontrado.")

        while True:
            continuar = input("¿Deseas actualizar otro cliente? (s/n): ").lower()
            if continuar == "s":
                break
            elif continuar == "n":
                print("Operacion terminada.")
                return
            else:
                print("Por favor, ingrese 's' o 'n'.")

def eliminar_cliente(clientes):
    while True:
        dni = input("Ingrese el DNI del cliente a eliminar: ")

        if not dni.isdigit():
            print("El DNI debe ser un numero valido.")
            continue

        dni = int(dni)

        cliente_encontrado = None
        for cliente in clientes:
            if cliente.dni == dni:
                cliente_encontrado = cliente
                break

        if cliente_encontrado:
            while True:
                confirmacion = input(f"¿Estas seguro de eliminar al cliente con DNI {dni}? (s/n): ").lower()

                if confirmacion == "s":
                    clientes.remove(cliente_encontrado)
                    print(f"Cliente con DNI {dni} eliminado con exito.")
                    break
                elif confirmacion == "n":
                    print("Eliminacion del cliente anulada.")
                    break
                else:
                    print("Por favor, ingrese 's' o 'n'.")
                    continue
        else:
            print(f"No se encontro un cliente con DNI {dni}.")

        while True:
            continuar = input("¿Desea eliminar otro cliente? (s/n): ").lower()
            if continuar == "s":
                break
            elif continuar == "n":
                print("Operacion terminada.")
                return
            else:
                print("Por favor, ingrese 's' o 'n'.")

def mezclar_por_dni(lista, inicio, medio, fin):
    izquierda = lista[inicio : medio + 1]
    derecha = lista[medio + 1 : fin + 1]

    i = j = 0
    k = inicio

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i].dni <= derecha[j].dni:
            lista[k] = izquierda[i]
            i += 1
        else:
            lista[k] = derecha[j]
            j += 1
        k += 1

    while i < len(izquierda):
        lista[k] = izquierda[i]
        i += 1
        k += 1

    while j < len(derecha):
        lista[k] = derecha[j]
        j += 1
        k += 1


def merge_sort_por_dni(lista, inicio, fin):
    if inicio < fin:
        medio = (inicio + fin) // 2
        merge_sort_por_dni(lista, inicio, medio)
        merge_sort_por_dni(lista, medio + 1, fin)
        mezclar_por_dni(lista, inicio, medio, fin)


def ordenar_clientes_por_dni(clientes):
    merge_sort_por_dni(clientes, 0, len(clientes) - 1)
    print("Clientes ordenados por DNI.")

#FUNCIONES PEDIDOS
def crear_pedido(pedidos, productos, clientes):
    while True:
        try:
            codigo_identificador_de_pedido = int(input("Ingrese el codigo identificador de pedido: "))
            if codigo_identificador_de_pedido <= 0:
                print("El codigo identificador de pedido debe ser un numero positivo. Intente nuevamente.")
                continue

            codigo_existente = False
            for pedido in pedidos:
                if pedido.codigo_identificador_de_pedido == codigo_identificador_de_pedido:
                    print("Ese codigo de pedido ya existe. Intente con otro.")
                    codigo_existente = True
                    break

            if not codigo_existente:
                break

        except ValueError:
            print("Debe ingresar un numero para el codigo identificador de pedido. Intente nuevamente.")
            continue

    while True:
        try:
            cliente_dni = int(input("Ingrese el DNI del cliente: "))
            cliente_obj = None
            for cliente in clientes:
                if cliente.dni == cliente_dni:
                    cliente_obj = cliente
                    break

            if cliente_obj:
                break
            else:
                print("Cliente no encontrado.")
                while True:
                    opcion = input("¿Desea buscar otro cliente? (s/n): ").lower()
                    if opcion == "s":
                        break
                    elif opcion == "n":
                        print("Operacion cancelada.")
                        return
                    else:
                        print("Por favor, ingrese 's' o 'n'.")

        except ValueError:
            print("Debe ingresar un numero valido para el DNI del cliente.")
            continue

    productos_seleccionados = []
    while True:
        try:
            codigo_ean_producto = int(input("Ingrese el codigo EAN del producto (0 para terminar): "))
            if codigo_ean_producto == 0:
                break
            producto = None
            for prod in productos:
                if prod.codigo_ean == codigo_ean_producto:
                    productos_seleccionados.append(prod)
                    producto = True
                    break
            if not producto:
                print("Producto no encontrado.")
                while True:
                    opcion = input("¿Desea intentar con otro codigo EAN? (s/n): ").lower()
                    if opcion == "s":
                        break
                    elif opcion == "n":
                        break
                    else:
                        print("Por favor, ingrese 's' o 'n'.")

        except ValueError:
            print("Debe ingresar un numero valido para el codigo EAN.")
            continue

    while True:
        fecha_pedido = input("Ingrese la fecha del pedido (DD/MM/AAAA): ")

        if fecha_pedido:
            dia, mes, anio = pedido.parse_fecha(fecha_pedido)
            if dia is not None:
                break
            else:
                print("Fecha invalida. Asegurese de ingresar el formato 'DD/MM/AAAA'.")
        else:
            print("Debe ingresar una fecha para el pedido. Por favor, ingrese una fecha valida.")

    while True:
        try:
            cargos_extra = float(input("Ingrese los cargos extra (puede ser negativo para descuento) (o tambien puedes poner 0 por si no quieres ningun descuento ni recargo): "))
            break
        except ValueError:
            print("Debe ingresar un valor numerico para los cargos extra. Intente nuevamente.")

    pedido = Pedido(
        codigo_identificador_de_pedido,
        productos_seleccionados,
        cliente_obj,
        fecha_pedido,
        cargos_extra,
    )
    pedidos.append(pedido)
    print("Pedido creado con exito.")

    while True:
        opcion = input("¿Desea agregar otro pedido? (s/n): ").lower()
        if opcion == "s":
            crear_pedido(pedidos, productos, clientes)
            break
        elif opcion == "n":
            print("Nos vemos.")
            break
        else:
            print("Por favor, ingrese 's' o 'n'.")

def consultar_todos_los_pedidos(pedidos):
    if not pedidos:
        print("No hay pedidos registrados.")
        return
    
    ordenar_pedidos_por_total(pedidos)
    print("Lista ya ordenada por importe total, de menor a mayor")
    for pedido in pedidos:
        print(f"Código: {pedido.codigo_identificador_de_pedido}, Cliente: {pedido.cliente.nombre_apellido}, Fecha: {pedido.fecha_pedido}, Total: ${pedido.calcular_total():.2f}")

def busqueda_binaria(lista, codigo_buscado):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        pedido = lista[medio]

        if pedido.codigo_identificador_de_pedido == codigo_buscado:
            return pedido 
        elif pedido.codigo_identificador_de_pedido < codigo_buscado:
            izquierda = medio + 1  
        else:
            derecha = medio - 1 

    return None  

def consultar_pedidos_por_codigo_identificador(pedidos):
    ordenar_pedidos_por_total(pedidos)  

    while True:
        try:
            codigo_a_buscar = int(input("Ingrese el codigo de pedido a consultar: "))
        except ValueError:
            print("Por favor, ingrese un número valido para el codigo del pedido.")
            continue

       
        pedido_encontrado = None
        for pedido in pedidos:
            if pedido.codigo_identificador_de_pedido == codigo_a_buscar:
                pedido_encontrado = pedido
                break

        if pedido_encontrado:
            print(f"Pedido encontrado: Codigo: {pedido_encontrado.codigo_identificador_de_pedido}, "
                  f"Cliente: {pedido_encontrado.cliente.nombre_apellido}, Fecha: {pedido_encontrado.fecha_pedido}, "
                  f"Total: ${pedido_encontrado.calcular_total():.2f}")
        else:
            print(f"No existe un pedido con codigo {codigo_a_buscar}")

        while True:
            continuar = input("¿Desea buscar otro pedido? (s/n): ").lower()
            if continuar == "s":
                break
            elif continuar == "n":
                print("Operacion terminada.")
                return
            else:
                print("Por favor, ingrese 's' o 'n'.")

def actualizar_pedido(pedidos, productos):
    while True:
        try:
            codigo_identificador = int(
                input("Ingrese el codigo de pedido a actualizar: ")
            )
        except ValueError:
            print("Por favor, ingrese un numero valido.")
            continue

        pedido = None
        for p in pedidos:
            if p.codigo_identificador_de_pedido == codigo_identificador:
                pedido = p
                break

        if not pedido:
            print("Pedido no encontrado.")
            while True:
                intentar_otra_vez = input(
                    "¿Quieres intentar buscando otro? (s/n): "
                ).lower()
                if intentar_otra_vez == "s":
                    break
                elif intentar_otra_vez == "n":
                    print("Operacion terminada.")
                    return
                else:
                    print("Por favor, ingrese 's' o 'n'.")
            continue  #volvemos a intentarlo de nuevo!

        # mostramos los detalles de ese pedido 
        print(
            f"Pedido encontrado: Cliente: {pedido.cliente.nombre_apellido}, Fecha: {pedido.fecha_pedido}, Total: ${pedido.calcular_total():.2f}"
        )

        # aca que nos confirme si quiere cambiar el pedido 
        while True:
            cambiar_codigo = input(
                "¿Desea cambiar el codigo de identificador del pedido? (s/n): "
            ).lower()
            if cambiar_codigo == "s":
                try:
                    nuevo_codigo_identificador = int(
                        input("Ingrese el nuevo codigo de identificador de pedido: ")
                    )
                    # verificamos que el codigo no este en uso 
                    for p in pedidos:
                        if (
                            p.codigo_identificador_de_pedido
                            == nuevo_codigo_identificador
                        ):
                            print("El codigo de identificador ya esta siendo usado.")
                            while True:
                                continuar = input(
                                    "¿Quieres intentar de nuevo? (s/n): "
                                ).lower()
                                if continuar == "s":
                                    break
                                elif continuar == "n":
                                    print("Operacion cancelada.")
                                    return
                                else:
                                    print("Por favor, ingrese 's' o 'n'.")
                            break
                    else:
                        pedido.codigo_identificador_de_pedido = (
                            nuevo_codigo_identificador
                        )
                        print(
                            f"El codigo de identificador ha sido actualizado a {nuevo_codigo_identificador}."
                        )
                        break

                except ValueError:
                    print("Valor de codigo no valido. No se actualizo el codigo.")
            elif cambiar_codigo == "n":
                break
            else:
                print("Por favor, ingrese 's' o 'n'.")

        # listo agregamos productos al pedido 
        productos_seleccionados = pedido.productos
        while True:
            try:
                codigo_ean_producto = int(
                    input(
                        "Ingrese el codigo EAN del producto a agregar al pedido (0 para terminar): "
                    )
                )
            except ValueError:
                print("Por favor, ingrese un codigo EAN valido.")
                continue

            if codigo_ean_producto == 0:
                break

            producto = None
            for prod in productos:
                if prod.codigo_ean == codigo_ean_producto:
                    producto = prod
                    break

            if producto:
                productos_seleccionados.append(producto)
                print(f"Producto {producto.nombre} agregado.")
            else:
                print("Producto no encontrado.")

        while True:
            nueva_fecha_pedido = input(
                f"Ingrese la nueva fecha del pedido (actual: {pedido.fecha_pedido}) (DD/MM/AAAA): "
            )

            if nueva_fecha_pedido:
                dia, mes, anio = pedido.parse_fecha(nueva_fecha_pedido)
                if dia is not None:
                    pedido.fecha_pedido = nueva_fecha_pedido
                    print(f"Fecha de pedido actualizada a {nueva_fecha_pedido}.")
                    break  # Sale del bucle cuando la fecha es válida
                else:
                    print(
                        "Fecha invalida. Asegurese de ingresar el formato 'DD/MM/AAAA'."
                    )
            else:
                print("No se ingreso una fecha. Se mantiene la fecha actual.")
                break  # Si no se ingresa nada, mantiene la fecha actual

        #actualizamos los cargos extra 
        try:
            nuevos_cargos_extra = input(
                f"Ingrese los nuevos cargos extra (actual: {pedido.cargos_extra}): "
            )
            if nuevos_cargos_extra:
                pedido.cargos_extra = float(nuevos_cargos_extra)
        except ValueError:
            print("Valor de cargos extra invalido. No se actualizo.")

        pedido.productos = productos_seleccionados
        print("Pedido actualizado con exito.")

        while True:
            continuar = input("¿Desea actualizar otro pedido? (s/n): ").lower()
            if continuar == "s":
                break
            elif continuar == "n":
                print("Operacion terminada.")
                return
            else:
                print("Por favor, ingrese 's' o 'n'.")

def eliminar_pedido(pedidos):
    while True:
        try:
            # solicitamos el codigo pedido y nos asegureamos que sea de tipo numero 
            codigo_identificador = int(
                input("Ingrese el codigo de pedido a eliminar: ")
            )

            pedido_encontrado = (
                False  # esto nos sirve por si encuentra el pedido 
            )
            for p in pedidos:
                if p.codigo_identificador_de_pedido == codigo_identificador:
                    pedido_encontrado = True  # listo encontro el pedidoo 
                    while True:
                        confirmar = input(
                            f"¿Estas seguro de eliminar el pedido con codigo {codigo_identificador}? (s/n): "
                        ).lower()
                        if confirmar == "s":
                            pedidos.remove(p)
                            print(
                                f"Pedido con codigo {codigo_identificador} eliminado exitosamente."
                            )
                            break  # listo salimos del ciclo y se elimina chau 
                        elif confirmar == "n":
                            print("Eliminación cancelada.")
                            break  # salimos si lo cancela tambien 
                        else:
                            print(
                                "Entrada no valida. Por favor ingrese 's' para confirmar o 'n' para cancelar."
                            )
                    break  # listo salimos del for 

            if not pedido_encontrado:
                # aca damos un error por si no encuentra el pedido 
                print(f"No existe un pedido con el código {codigo_identificador}.")

        except ValueError:
            print("Debe ingresar un numero valido para el codigo de pedido.")
            continue  # volvemos a pedir el codigo si lo que ingresa no es de tipo numero 

        while True:
            continuar = input("¿Desea eliminar otro pedido? (s/n): ").lower()
            if continuar == "s":
                break 
            elif continuar == "n":
                print("Operacion terminada.")
                return 
            else:
                print("Por favor, ingrese 's' o 'n'.")

def mezclar_por_total(lista, inicio, medio, fin):
    izquierda = lista[inicio : medio + 1]
    derecha = lista[medio + 1 : fin + 1]

    i = j = 0
    k = inicio

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i].calcular_total() <= derecha[j].calcular_total():
            lista[k] = izquierda[i]
            i += 1
        else:
            lista[k] = derecha[j]
            j += 1
        k += 1

    while i < len(izquierda):
        lista[k] = izquierda[i]
        i += 1
        k += 1

    while j < len(derecha):
        lista[k] = derecha[j]
        j += 1
        k += 1

def merge_sort_por_total(lista, inicio, fin):
    if inicio < fin:
        medio = (inicio + fin) // 2

        merge_sort_por_total(lista, inicio, medio)
        merge_sort_por_total(lista, medio + 1, fin)

        mezclar_por_total(lista, inicio, medio, fin)

def ordenar_pedidos_por_total(pedidos):
    merge_sort_por_total(pedidos, 0, len(pedidos) - 1)
    print("Pedidos ordenados por total.")