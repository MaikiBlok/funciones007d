def conversion_notas(puntaje,puntaje_total):
    nota= (puntaje * 6 / puntaje_total) +1
    return round(nota,1)
while True:
    try:
        p = float(input("Ingrese el puntaje obtenido:"))
        if p<0:
            print("El valor no es válido")
        else:
            break
    except ValueError:
        print("Favor ingresar un valor.")
while True:
    try:
        pt = float(input("Ingrese el puntaje máximo:"))
        if p<0:
            print("El valor no es válido")
        else:
            break
    except ValueError:
        print("Favor ingresar un valor númerico.")
print(f"El estudiante obtuvo una nota de {conversion_notas(p,pt)}")