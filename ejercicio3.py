def producto(nombre,precio,stock):
    print(f"Nombre: {nombre}")
    print(f"Precio: ${precio}")
    print(f"Stock:{stock}")
a=input("Ingrese el nombre del producto:")
while True:
    try:
        b=int(input("Ingrese el stock del producto"))
        if b<0:
            print("Debe de ser mayor o igual a cero.")
        else:
            break
    except ValueError:
        print("Debe ingresar numeros.")
    
while True:
    try:
        c=int(input("Ingrese el precio:"))
        if c<=0:
            print("Debe ser un numero positivo.")
        else:
            break
    except ValueError:
        print("Debe ingresar numeros.")
producto(a,c,b)