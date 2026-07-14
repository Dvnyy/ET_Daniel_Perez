from diccionario import arreglos, bodega

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por tipo de arreglo")
    print("2. Búsqueda de arreglos por rango de precio")
    print("3. Actualizar precio de arreglo")
    print("4. Agregar arreglo")
    print("5. Eliminar arreglo")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    opcion_valida = False
    while not opcion_valida:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion >= 1 and opcion <= 6:
                opcion_valida = True
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")
    return opcion

def unidades_tipo(tipo, arreglos, bodega):
    total = 0
    for codigo in arreglos:
        tipo_arreglo = arreglos[codigo][1]
        if tipo_arreglo.lower() == tipo.lower():
            total = total + bodega[codigo][1]
    print("El total de unidades disponibles es:", total)

def busqueda_precio(p_min, p_max, arreglos, bodega):
    resultados = []
    for codigo in bodega:
        precio = bodega[codigo][0]
        unidades = bodega[codigo][1]
        if precio >= p_min and precio <= p_max and unidades != 0:
            nombre = arreglos[codigo][0]
            resultados.append(nombre + "-" + codigo)

    resultados.sort()

    if len(resultados) == 0:
        print("No hay arreglos en ese rango de precios.")
    else:
        print("Los arreglos encontrados son:", resultados)

def buscar_codigo(codigo, diccionario):
    codigo = codigo.upper()
    encontrado = False
    for clave in diccionario:
        if clave.upper() == codigo:
            encontrado = True
    return encontrado

def actualizar_precio(codigo, nuevo_precio, bodega):
    codigo = codigo.upper()
    if buscar_codigo(codigo, bodega):
        bodega[codigo][0] = nuevo_precio
        return True
    else:
        return False

def validar_texto(texto):
    return texto.strip() != ""

def validar_tamano(tamano):
    return tamano == "S" or tamano == "M" or tamano == "L"

def validar_tarjeta(valor):
    return valor == "s" or valor == "n"

def validar_precio(precio):
    return precio > 0

def validar_unidades(unidades):
    return unidades >= 0

def agregar_arreglo(codigo, nombre, tipo, color_principal, tamano,
                    incluye_tarjeta, temporada, precio, unidades,
                    arreglos, bodega):
    codigo = codigo.upper()
    if buscar_codigo(codigo, arreglos):
        return False
    else:
        arreglos[codigo] = [nombre, tipo, color_principal, tamano,
                            incluye_tarjeta, temporada]
        bodega[codigo] = [precio, unidades]
        return True

def eliminar_arreglo(codigo, arreglos, bodega):
    codigo = codigo.upper()
    if buscar_codigo(codigo, arreglos):
        del arreglos[codigo]
        del bodega[codigo]
        return True
    else:
        return False

def main():
    opcion = 0

    while opcion != 6:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            tipo = input("Ingrese tipo de arreglo a consultar: ")
            unidades_tipo(tipo, arreglos, bodega)

        elif opcion == 2:
            valores_validos = False
            while not valores_validos:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        valores_validos = True
                    else:
                        print("Debe ingresar valores enteros")
                except ValueError:
                    print("Debe ingresar valores enteros")

            busqueda_precio(p_min, p_max, arreglos, bodega)

        elif opcion == 3:
            respuesta = "s"
            while respuesta == "s":
                codigo = input("Ingrese código del arreglo: ")

                precio_valido = False
                while not precio_valido:
                    try:
                        nuevo_precio = int(input("Ingrese nuevo precio: "))
                        if validar_precio(nuevo_precio):
                            precio_valido = True
                        else:
                            print("El precio debe ser un entero positivo")
                    except ValueError:
                        print("Debe ingresar un valor entero")

                if actualizar_precio(codigo, nuevo_precio, bodega):
                    print("Precio actualizado")
                else:
                    print("El código no existe")

                respuesta = input("¿Desea actualizar otro precio (s/n)?: ")

        elif opcion == 4:
            codigo = input("Ingrese código del arreglo: ")
            nombre = input("Ingrese nombre: ")
            tipo = input("Ingrese tipo: ")
            color_principal = input("Ingrese color principal: ")
            tamano = input("Ingrese tamaño (S/M/L): ")
            tarjeta_texto = input("¿Incluye tarjeta? (s/n): ")
            temporada = input("Ingrese temporada: ")

            precio_es_entero = True
            try:
                precio = int(input("Ingrese precio: "))
            except ValueError:
                precio_es_entero = False
                precio = 0

            unidades_es_entero = True
            try:
                unidades = int(input("Ingrese unidades: "))
            except ValueError:
                unidades_es_entero = False
                unidades = 0

            if not validar_texto(codigo):
                print("El código no puede estar vacío")
            elif buscar_codigo(codigo, arreglos):
                print("El código ya existe")
            elif not validar_texto(nombre):
                print("El nombre no puede estar vacío")
            elif not validar_texto(tipo):
                print("El tipo no puede estar vacío")
            elif not validar_texto(color_principal):
                print("El color principal no puede estar vacío")
            elif not validar_tamano(tamano):
                print("El tamaño debe ser S, M o L")
            elif not validar_tarjeta(tarjeta_texto):
                print("Debe ingresar s o n")
            elif not validar_texto(temporada):
                print("La temporada no puede estar vacía")
            elif not precio_es_entero or not validar_precio(precio):
                print("El precio debe ser un número entero mayor que cero")
            elif not unidades_es_entero or not validar_unidades(unidades):
                print("Las unidades deben ser un número entero mayor o igual a cero")
            else:
                incluye_tarjeta = (tarjeta_texto == "s")
                agregado = agregar_arreglo(codigo, nombre, tipo, color_principal,
                                           tamano, incluye_tarjeta, temporada,
                                           precio, unidades, arreglos, bodega)
                if agregado:
                    print("Arreglo agregado")
                else:
                    print("El código ya existe")

        elif opcion == 5:
            codigo = input("Ingrese código del arreglo a eliminar: ")
            if eliminar_arreglo(codigo, arreglos, bodega):
                print("Arreglo eliminado")
            else:
                print("El código no existe")

        elif opcion == 6:
            print("Programa finalizado.")


if __name__ == "__main__":
    main()