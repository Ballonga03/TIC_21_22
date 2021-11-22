def piramide_numerica():
    
    num=input("Dame un numero: ")
    for cont in range(num,0,-1):
        print str(cont)*cont

piramide_numerica()
