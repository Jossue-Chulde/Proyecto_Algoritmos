from tkinter import *
import tkinter as tk

ventana = tk.Tk()
ventana.title("Rutas Turisticas")
ventana.geometry("500x500")
ventana.mainloop()

usuarios = []

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
