# Esercizio python: Si scriva un programma che in base alla scelta dell'utente 
#permetta di calcolare il perimetro delle diverse figure geometriche (quadrato, cerchio, rettangolo)


#Questo programma utilizza una semplice struttura di controllo if-elif-else 
#per gestire la scelta dell'utente e calcola il perimetro della figura geometrica selezionata. 
#Il loop while True consente all'utente di effettuare più calcoli senza dover riavviare 
#il programma ogni volta.

import math 

while True:
    
    print("Scegli la figura geometrica di cui vuoi sapere il perimetro:\n")
    print("1. Quadrato")
    print("2. Cerchio")
    print("3. Rettangolo \n")

         
    scelta= input("scegli tra le varie opzioni 1, 2, 3 : ")

    if scelta == "1":
        l=float(input("Inserisci il lato del quadrato: "))
        print("Il perimetro del quadrato è: ", l*4)    
    
    elif scelta == "2":
        r=float(input("Inserisci il raggio del cerchio: "))
        print("La circonferenza è: ", 2*math.pi*r)
    
    elif scelta == "3":
        base = float(input("Inserisci la base del rettangolo: "))
        altezza = float(input("Inserisci l'altezza del rettangolo: "))
        print("Il perimetro del rettangolo è: ", base*2 + altezza*2)
            
    else:
        print("La tua scelta non è tra quelle disponibili, riprova ")
    
    continuare= input("Vuoi fare un'altra operazione? (si/no)  ")
    
    if continuare.lower() !="si":
        break
    