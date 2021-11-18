def diagrama():
    num=input("dame un numero: ")
    sum=1
    for cont in range(num,0,-1):
        print cont,sum
        sum=sum*cont

diagrama()
    
