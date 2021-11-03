def contador_palabras():
    palabra=input("dime una palabra: ")
    vocales="V"
    consonantes="C"
    Si="S"
    No="N"
    while(continuar=="V/C"):
        num_vocales=input("dime una palabra: ")
        suma_vocales=suma_vocales+num_vocales
        continuar=raw_input("Quieres leer otra palabra? (S/N): ")
    print("SUMA= "+str(suma))

contador_palabras()
