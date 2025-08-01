import os 

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        lineas = []
        for linea in archivo:
            lineas.append(linea.strip())
        archivo.close()
        return lineas
        
def escribir_archivo(nombre_archivo, datos):
    with open(nombre_archivo, "w") as archivo:
        for dato in datos:
            archivo.write(dato + "\n")
        archivo.close()

def validar_gmail(email):
    if "@gmail.com" not in email:
        return False

    partes = email.split("@gmail.com")
    if len(partes) != 2:
        return False

    if partes[1] != "":
        return False

    if partes[0] == "":
        return False

    return True
    
def validar_contrasena(password):
    mayusculas = False
    minusculas = False
    numeros = False

    for char in password:
        if char >= 'A' and char <= 'Z':
            mayusculas = True
        if char >= 'a' and char <= 'z':
            minusculas = True
        if char >= '0' and char <= '9':
            numeros = True

    return mayusculas and minusculas and numeros

def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def ordenar_insercion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = actual
    return lista

def dijkstra(grafo, inicio, fin):
    ciudades = list(grafo.keys())
    distancias = {}
    padres = {}

    for ciudad in ciudades:
        distancias[ciudad] = 999999
        padres[ciudad] = None
    distancias[inicio] = 0

    visitadas = []

    for _ in range(len(ciudades)):
        actual = None
        menor = 999999
        for ciudad in ciudades:
            if ciudad not in visitadas and distancias[ciudad] < menor:
                menor = distancias[ciudad]
                actual = ciudad

        if actual is None:
            break

        visitadas.append(actual)

        if actual in grafo:
            for vecino, costo in grafo[actual].items():
                nueva_dist = distancias[actual] + costo
                if nueva_dist < distancias[vecino]:
                    distancias[vecino] = nueva_dist
                    padres[vecino] = actual

    camino = []
    actual = fin
    while actual is not None:
        camino.append(actual)
        actual = padres[actual]
    camino.reverse()

    if distancias[fin] == 999999:
        return None, 0
    return camino, distancias[fin]

def registrar():
    print("=== REGISTRO ===")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cedula = input("Cédula: ")
    edad = input("Edad: ")
    email = input("Email: ")
    while not validar_gmail(email):
        print("Debe ser un correo de Gmail (@gmail.com)")
        email = input("Email: ")

    password = input("Contraseña: ")
    while not validar_contrasena(password):
        print("Debe tener mayúscula, minúscula y número")
        password = input("Contraseña: ")

    linea = nombre + "," + apellido + "," + cedula + "," + edad + "," + email + "," + password
    usuarios = leer_archivo("usuarios.txt")
    usuarios.append(linea)
    escribir_archivo("usuarios.txt", usuarios)
    print("¡Registrado!")

def login():
    print("=== POLI TOURS ===")
    email = input("Ingrese su correo electronico: ")
    password = input("Ingrese su contraseña: ")

    usuarios = leer_archivo("usuarios.txt")
    for usuario in usuarios:
        datos = usuario.split(",")
        if len(datos) >= 6 and datos[4] == email and datos[5] == password:
            print("¡Bienvenido " + datos[0] + "!")
            return datos

    print("Contraseña o Usuario incorectos vuelva a intentarlo mas tarde")
    return None #Representa a nada o valor vacio si no se encuentra el usuario

def menu_administrador():
    while True:
        print("\n=== Menu Administrador ===")
        print("1. Agregar Nueva Ciudad/Punto Turistico")
        print("2. Listar Ciudades/Puntos Turisticos")
        print("3. Consultar Ciudad/Punto Turistico")
        print("4. Actualizar Ciudad/Punto Turistico")
        print("5. Eliminar Ciudad/Punto Turistico")
        print("6. Salir del Programa")
        try:
            opcion = int(input("Seleccione una Opción: "))
            if opcion == 1:
                agregar_ruta()
            elif opcion == 2:
                ver_rutas()
            elif opcion == 3:
                buscar_ruta()
            elif opcion == 4:
                actualizar_ruta()
            elif opcion == 5:
                eliminar_ruta()              
            elif opcion == 6:
                print("Saliendo del Menu de Administrador")
                break
            else:
                print("Opción no válida")
        except ValueError:
            print("Solo digite un numero")
            continue  
            
def agregar_ruta():
    print("=== Rutas del POLI TOURS ===")
    origen = input("Ruta de origen del viaje: ")
    destino = input("Ruta de destino del viaje: ")
    distancia = input("Distancia total del viaje: ")
    costo = input("Costo del viaje: ")

    linea = origen + "," + destino + "," + distancia + "," + costo
    rutas = leer_archivo("rutas.txt")
    rutas.append(linea)
    escribir_archivo("rutas.txt", rutas)
    print("La ruta ha sido agregada con exito")

def ver_rutas():
    print("=== RUTAS ===")
    rutas = leer_archivo("rutas.txt")
    rutas_ordenadas = ordenar_burbuja(rutas.copy())

    for ruta in rutas_ordenadas:
        datos = ruta.split(",")
        if len(datos) >= 4:
            print(datos[0] + " -> " + datos[1] + " | $" + datos[3])
                  
def buscar_ruta():
    print("=== BUSCAR ===")
    ciudad = input("Ciudad: ")

    rutas = leer_archivo("rutas.txt")
    encontradas = []

    for ruta in rutas:
        if ciudad in ruta:
            encontradas.append(ruta)

    if len(encontradas) > 0:
        print("Encontradas:")
        for ruta in encontradas:
            datos = ruta.split(",")
            if len(datos) >= 4:
                print(datos[0] + " -> " + datos[1] + " | $" + datos[3])
    else:
        print("No encontradas")

def actualizar_ruta():
    print("=== ACTUALIZAR ===")
    origen = input("Origen: ")
    destino = input("Destino: ")

    rutas = leer_archivo("rutas.txt")

    for i in range(len(rutas)):
        datos = rutas[i].split(",")
        if len(datos) >= 4 and datos[0] == origen and datos[1] == destino:
            print("Ruta actual:", rutas[i])
            nueva_distancia = input("Nueva distancia: ")
            nuevo_costo = input("Nuevo costo: ")

            rutas[i] = origen + "," + destino + "," + nueva_distancia + "," + nuevo_costo
            escribir_archivo("rutas.txt", rutas)
            print("¡Actualizada!")
            return

    print("No encontrada")

def eliminar_ruta():
    print("=== ELIMINAR ===")
    origen = input("Origen: ")
    destino = input("Destino: ")

    rutas = leer_archivo("rutas.txt")

    for i in range(len(rutas)):
        datos = rutas[i].split(",")
        if len(datos) >= 4 and datos[0] == origen and datos[1] == destino:
            rutas.pop(i)
            escribir_archivo("rutas.txt", rutas)
            print("¡Eliminada!")
            return
    print("No encontrada")
    
def menu_usuario(usuario):
    mis_ciudades = []
    while True:
        print("\n=== Menu Usuario ===")
        print("1. Ver mapa de lugares turísticos conectados")
        print("2. Consultar la ruta óptima entre dos ciudades/puntos turísticos y el costo")
        print("3. Seleccionar Ciudades/Punto Turisticos a visitar")
        print("4. Listar la o las ciudades/puntos turísticos y el costo total")
        print("5. Guardar la selección de Ciudades/Punto Turisticos")
        print("6. Salir del Programa")
        try:
            opcion = int(input("Seleccione una Opción: "))
            if opcion == 1:
                ver_ciudades()
            elif opcion == 2:
                ruta_optima()
            elif opcion == 3:
                seleccionar_ciudades(mis_ciudades)
            elif opcion == 4:
                ver_seleccion(mis_ciudades)
            elif opcion == 5:
                guardar_itinerario(usuario, mis_ciudades)
            elif opcion == 6:
                print("Saliendo del Menu de Usuarios")
                break
            else:
                print("Opción no válida")
        except ValueError:
            print("Solo digite un numero")
            continue        

def ver_ciudades():
    print("=== CIUDADES TURISTICAS ===")
    rutas = leer_archivo("rutas.txt")
    ciudades = []

    for ruta in rutas:
        datos = ruta.split(",")
        if len(datos) >= 2:
            if datos[0] not in ciudades:
                ciudades.append(datos[0])
            if datos[1] not in ciudades:
                ciudades.append(datos[1])

    ciudades_ordenadas = ordenar_insercion_sort(ciudades)

    for i in range(len(ciudades_ordenadas)):
        print(str(i + 1) + ". " + ciudades_ordenadas[i])

def ruta_optima():
    print("=== RUTA ÓPTIMA ===")

    grafo = {}
    rutas = leer_archivo("rutas.txt")

    for ruta in rutas:
        datos = ruta.split(",")
        if len(datos) >= 4:
            origen = datos[0]
            destino = datos[1]
            costo = float(datos[3])

            if origen not in grafo:
                grafo[origen] = {}
            if destino not in grafo:
                grafo[destino] = {}

            grafo[origen][destino] = costo
            grafo[destino][origen] = costo

    ciudades = list(grafo.keys())
    for i in range(len(ciudades)):
        print(str(i + 1) + ". " + ciudades[i])

    origen = input("Ciudad origen: ")
    destino = input("Ciudad destino: ")

    camino, costo = dijkstra(grafo, origen, destino)

    if camino:
        print("Mejor ruta:")
        ruta_texto = ""
        for i in range(len(camino)):
            ruta_texto += camino[i]
            if i < len(camino) - 1:
                ruta_texto += " -> "
        print(ruta_texto)
        print("Costo: $" + str(costo))
    else:
        print("No se pudo encontrar una ruta")

def seleccionar_ciudades(mis_ciudades):
    print("=== SELECCIONAR ===")

    rutas = leer_archivo("rutas.txt")
    ciudades = []

    for ruta in rutas:
        datos = ruta.split(",")
        if len(datos) >= 2:
            if datos[0] not in ciudades:
                ciudades.append(datos[0])
            if datos[1] not in ciudades:
                ciudades.append(datos[1])

    print("Ciudades disponibles:")
    for i in range(len(ciudades)):
        print(str(i + 1) + ". " + ciudades[i])

    while True:
        ciudad = input("Ciudad a agregar o fin: ")
        if ciudad == "fin":
            break

        if ciudad in ciudades and ciudad not in mis_ciudades:
            mis_ciudades.append(ciudad)
            print("Agregada: " + ciudad)
        elif ciudad in mis_ciudades:
            print("Ya está seleccionada")
        else:
            print("No existe")

def ver_seleccion(mis_ciudades):
    print("=== SELECCION DE USUARIO  ===")

    if len(mis_ciudades) == 0:
        print("No hay ciudades seleccionadas")
        return
    ciudades_ordenadas = ordenar_insercion_sort(mis_ciudades.copy())

    print("Ciudades:")
    for i in range(len(ciudades_ordenadas)):
        print(str(i + 1) + ". " + ciudades_ordenadas[i])

    print("Total: " + str(len(mis_ciudades)))

def guardar_itinerario(usuario, mis_ciudades):
    print("=== GUARDAR ===")

    if len(mis_ciudades) == 0:
        print("No hay ciudades")
        return

    nombre_archivo = "itinerario-" + usuario[0] + "-" + usuario[1] + ".txt"

    itinerario = []
    itinerario.append("ITINERARIO DE " + usuario[0] + " " + usuario[1])
    itinerario.append("Email: " + usuario[4])
    itinerario.append("=" * 30)
    itinerario.append("")
    itinerario.append("CIUDADES:")

    for i in range(len(mis_ciudades)):
        itinerario.append(str(i + 1) + ". " + mis_ciudades[i])

    itinerario.append("")
    itinerario.append("Total: " + str(len(mis_ciudades)))

    escribir_archivo(nombre_archivo, itinerario)
    print("Guardado en: " + nombre_archivo)

def main():
    print("PoliTours")

    if not os.path.exists("usuarios.txt"):
        usuarios_iniciales = ["Admin,Sistema,0000000000,30,admin@politours.com,Admin123"]
        escribir_archivo("usuarios.txt", usuarios_iniciales)

    if not os.path.exists("rutas.txt") or os.path.getsize("rutas.txt") == 0:
        rutas_iniciales = [
            "Quito,Guayaquil,421,25.5",
            "Quito,Cuenca,430,28.0",
            "Guayaquil,Cuenca,197,15.0",
            "Quito,Ambato,128,10.0",
            "Ambato,Baños,40,5.0"
        ]
        escribir_archivo("rutas.txt", rutas_iniciales)

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Login Cliente")
        print("2. Registro")
        print("3. Login Admin")
        print("4. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            usuario = login()
            if usuario and usuario[4] != "admin@politours.com":
                menu_usuario(usuario)

        elif opcion == "2":
            registrar()

        elif opcion == "3":
            email = input("Email admin: ")
            password = input("Password admin: ")
            if email == "admin@politours.com" and password == "Admin123":
                menu_administrador()
            else:
                print("Datos incorrectos")

        elif opcion == "4":
            print("Saliendo del sistema")
            break

main()
