def menu():
    #Pedimos dos numeros
    num1=input("Introduce un numero: ")
    num2=input("Introduce otro numero: ")
    print("****************************")
    print("*          MENU            *")
    print("****************************")
    print("1. SUMAR")
    print("2. RESTAR")
    print("3. MULTIPLICAR")
    print("4. DIVIDION")
    opcion=0
    while(opcion<=0 or opcion>4):
        opcion=input(" ELIGE: ")
    print("Has elgido la opcion "+str(opcion))
    #OPCION SUMA
    if(opcion==1):
        print(num1+num2)
    #OPCION RESTA
    if(opcion==2):
        print(num1-num2)
    #POCION PRODUCTO
    if(opcion==3):
        print(num1*num2)
    #OPCION COCIENTE
    if(opcion==4):
        print(float(num1)/num2)

menu()
