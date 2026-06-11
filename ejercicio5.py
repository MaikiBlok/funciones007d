def encabezado():
    print("ENCABEZADO")
def solicitar_datos():
    estudiantes={}
    estudiantes["Rut"]=input("Ingrese el rut del estudiante:")
    estudiantes["Nombre"]=(input("Ingrese el nombre del estudiante:"))
    estudiantes["Carrera"]=input("Ingrese la carrera perteneciente:")
    while True:
        try:
            estudiantes["Semestre"]=int(input("En que semestre se encuentra:"))
            if estudiantes["Semestre"]<1 or estudiantes["Semestre"]>4:
                print("Favor ingresar un valor valido (1-4).")
            else:
                break
        except ValueError:
            print("Favor ingresar un valor numerico")
    return estudiantes
def mostrar_datos(alumnos):
    print(f"Nombre del estudiante:{alumnos["Nombre"]}")
    print(f"Rut del estudiante:{alumnos["Rut"]}")
    print(f"Carrera:{alumnos["Carrera"]}")
    print(f"Semestre actual:{alumnos["Semestre"]}")
datos=solicitar_datos()
encabezado()
mostrar_datos(datos)