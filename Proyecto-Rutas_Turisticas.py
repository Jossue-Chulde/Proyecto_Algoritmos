usuarios = []

Admin_Usuario = "admin@gmail.com"
Admin_contrasena = "Admin123"

def login():
    while True:
        print("\n==== POLI TOURS ====")
        print("1. Iniciar Sesión")
        print("2. Registrarse")
        print("3. Salir del Programa")
        try:
            opcion = int(input("Seleccione una Opción: "))
            if opcion == 1:
                inicio_de_sesion()
            elif opcion == 2:
                registrar_usuario()
            elif opcion == 3:
                print("Saliendo del programa")
                break
            else:
                print("Opción no válida")
        except ValueError:
            print("Solo digite un numero")
            continue                

def inicio_de_sesion():
    print("\n==== INICIO DE SESIÓN ====")
    usuario = input("Ingrese su correo: ")
    contrasena = input("Ingrese su contraeña: ")

    if usuario == Admin_Usuario and contrasena == Admin_contrasena:
        print("--- Incio de Sesión Exitosa ---")
        print("Bienvenido Administrador")
        menu_administrador()
        return "admin"

    for usuario_registrado in usuarios:
        if usuario_registrado["usuario"] == usuario and usuario_registrado["contraseña"] == contrasena:
            print("--- Incio de Sesión Exitosa ---")
            print("Bienvenido Usuario")
            menu_usuario()
            return "usuario"
    print("\nCredenciales Incorrectas")
    return None

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

def registrar_usuario():
    print("\n=== REGISTRO DE USUARIO ===")
    cedula = input("Ingrese su cédula: ")
    for usuario in usuarios:
        if usuario["cedula"] == cedula:
            print("usuario ya registrado")
            return None

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    usuario = input("Ingrese su email (formato: nombre.apellido@gmail.com): ")
    contrasena = input("Ingrese su contraseña: ")

    nuevo_usuario = {"cedula": cedula,"nombre": nombre,"apellido": apellido,"edad": edad,"usuario": usuario,"contraseña": contrasena}

    usuarios.append(nuevo_usuario)
    print("Usuario registrado exitosamente!")
    return nuevo_usuario

# MENU PRINCIPAL
login()
