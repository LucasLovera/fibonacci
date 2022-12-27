esValido = False
while not esValido:
    try:
        limite= int(input("Ingrese un limite: "))
        if limite >1:
            esValido = True
        else:
            print('El numero tiene que ser mayor a uno')
    except ValueError:
            print('Dato ingresado incorrecto, intente de nuevo')
            
    primer=int(input("primer numero: "))
    segundo=int(input("segundo numero: "))
    suma=primer + segundo
    c=1
    print("Fibonacci: ")
    print(primer)   
    print(segundo)

    while(c<=limite-2):    
        print(suma)
        c+=1
        primero=segundo
        segundo=suma
        suma=primero+segundo

