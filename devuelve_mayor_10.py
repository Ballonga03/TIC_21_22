def devuelve_mayor_10():
    mayor= input("Introduce un numero: ")
    for cont in range(1,10):
        num=input("Introduce un numero:")
        if(num>mayor):
            maor=num
    print("MAYOR= "+str(mayor))

devuelve_mayor_10()
