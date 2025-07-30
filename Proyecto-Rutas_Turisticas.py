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

def buscar_lineal(lista, valor):
    for i in range(len(lista)):
        if valor in lista[i]:
            return i
    return -1

def buscar_binaria(lista, valor):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if valor in lista[medio]:
            return medio
        elif lista[medio] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

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

    password = input("Contraseña: ")
    while not validar_contrasena(password):
        print("Debe tener mayúscula, minúscula y número")
        password = input("Contraseña: ")

    linea = nombre + "," + apellido + "," + cedula + "," + edad + "," + email + "," + password
    usuarios = leer_archivo("usuarios.txt")
    usuarios.append(linea)
    escribir_archivo("usuarios.txt", usuarios)
    print("¡Registrado!")

Admin_Usuario = "admin@gmail.com"
Admin_contrasena = "Admin123"

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
        print("6. Guardar Ciudad/Punto Turistico")
        print("7. Salir del Programa")
        try:
            opcion = int(input("Seleccione una Opción: "))
            if opcion == 1:
                print("Falta")
            elif opcion == 2:
                print("Falta")
            elif opcion == 3:
                print("Falta")
            elif opcion == 4:
                print("Falta")
            elif opcion == 5:
                print("Falta")
            elif opcion == 6:
                print("Falta")              
            elif opcion == 7:
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

def menu_usuario():
    while True:
        print("\n=== Menu Usuario ===")
        print("1. Ver mapa de lugares turísticos conectados")
        print("2. Consultar la ruta óptima entre dos ciudades/puntos turísticos y el costo")
        print("3. Explorar Lugares")
        print("4. Seleccionar Ciudades/Punto Turisticos a visitar")
        print("5. Listar la o las ciudades/puntos turísticos y el costo total")
        print("6. Actualizar la o las Ciudades/Punto Turisticos")
        print("7. Eliminar la o las Ciudades/Punto Turisticos") 
        print("8. Guardar la selección de Ciudades/Punto Turisticos")
        print("9. Salir del Programa")
        try:
            opcion = int(input("Seleccione una Opción: "))
            if opcion == 1:
                print("Falta")
            elif opcion == 2:
                print("Falta")
            elif opcion == 3:
                print("Falta")
            elif opcion == 4:
                print("Falta")
            elif opcion == 5:
                print("Falta")
            elif opcion == 6:
                print("Falta")
            elif opcion == 7:
                print("Falta")
            elif opcion == 8:
                print("Falta")      
            elif opcion == 9:
                print("Saliendo del Menu de Usuarios")
                break
            else:
                print("Opción no válida")
        except ValueError:
            print("Solo digite un numero")
            continue        

# MENU PRINCIPAL
login()
