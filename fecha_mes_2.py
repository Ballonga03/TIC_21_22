def fecha_mes_2():
    fecha=raw_input("Introduce la fecha (dd/mm/aa): ")
    nombre_meses="Enero,Febrero,Marzo,Abril,Mayo,Junio,Julio,Agosto,Septiembre,Octubre,Noviembre,Diciembre"
    numero_mes=fecha[3]*10+fecha[4]
    print("Numero_mes "+str(nuemro_mes))
    numero_comas=0
    cont=0
    while(numero_comas<=numero_mes-1):
        if(nombres_meses[cont]==','):
            numero_comas=numero_comas+1
        cont=cont+1
    print(cont)
    
fecha_mes_2()
