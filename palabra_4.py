def palabra_4():
    nombre=raw_input("NOMBRE:")
    apellido=raw_input("APELLIDO: ")
    print("Buenos dias, "+nombre+" "+apellido)
    print("Tu lindo nombre empieza con la letra "+nombre[0])
    print("Voy a deletrear tu nombre")
    for cont in range(0,20):
        print(nombre[cont])
    
palabra_4()
