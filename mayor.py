def mayor():
    total = mayor = menor = input("edad 1 ")
    for cont in range(1,3):
        edad = input("escribe tu edad")
        if edad > mayor:
            mayor=edad
        if edad < menor:
            menor=edad
        total=total+edad
    print mayor
    print menor
    print total/3
mayor()
    
        
