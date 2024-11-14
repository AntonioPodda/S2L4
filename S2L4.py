import math
print("Ciao!! Scegli una figura geometrica e ti dirò il suo perimetro!!: \n Quadrato? \n Cerchio? \n Rettangolo?")


scelta = input("INSERISCI LA FIGURA DI CUI VUOI SAPERE IL PERIMETRO: ")
if scelta == "quadrato":
    lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
    print("Il perimetro del quadrato è di:", lato * 4,"cm")

if scelta =="cerchio":
    raggio= float(input("Inserisci il raggio del cerchio: "))
    print("La circonferenza del cerchio è di:", 2 * math.pi * raggio)

if scelta == "rettangolo":
    base = float(input("Inserisci la base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    print("Il perimetro del rettangolo è:", 2 * (base + altezza))



