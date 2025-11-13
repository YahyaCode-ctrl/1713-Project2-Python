#Funcions:

def calcul_de_area_cudrat():
    print("--- ÀREA DEL QUADRAT ---")
    medida = float(input('Introdueix la longitud del costat del quadrat: '))
    area = medida * medida
    print("L'àrea del quadrat és:", area, "cm2")

def ets_menor_o_major():
    print("--- EDAT ---")
    nom = input("Com et dius? ")
    edat = int(input("Quants anys tens? ")) 

    if edat >= 18:
        print(f"{nom}, amb {edat} anys ets major d'edat")
    else:
        print(f"{nom}, amb {edat} anys ets menor d'edat")

def comparar_nums():
    print("--- COMPARAR 3 NÚMEROS ---")
    text1 = int(input('Introdueix el primer numero: '))
    text2 = int(input('Introdueix el segon numero: '))
    text3 = int(input('Introdueix el tercer numero: '))

    if text1 > text2 and text1 > text3:
        print(text1, "es el major")
    elif text2 >= text1 and text2 >= text3:
        print(text2, "es el major")
    elif text3 >= text1 and text3 >= text2:
        print(text3, "es el major")

def calculadora():
    print('\n--- CALCULADORA DE YAHYA ELHADRI ---')
    
    text1 = input('Introdueix el primer numero: ')
    text2 = input('Introdueix el segon numero: ')
    text3 = input("Tria l'operacio que vols fer ( + , - , * , / ): ")
    
    
    n1 = float(text1)
    n2 = float(text2)

    if text3 == '+':
        print('Suma:', n1 + n2)
    elif text3 == '-':
        print('Resta:', n1 - n2)
    elif text3 == '*':
        print('Multiplicacio:', n1 * n2)
    elif text3 == '/':
        if n2 != 0:
            print('Divisio:', n1 / n2)
        else:
            print("No es pot dividir per zero!")
    else:
        print('Operacio no valida')

def negatiu_o_positiu():
    print("\n--- POSITIU O NEGATIU ---")
    numero = int(input("Introdueix un numero: "))

    if numero >= 0:
        print(numero, "és positiu +")
    elif numero < 0:
        print(numero, "és negatiu -")
def main():
   while True:
        print(" ------ MENÚ D'EXERCICIS ------")
        print("1. Àrea del Quadrat")
        print("2. Major o Menor d'edat")
        print("3. Comparar 3 números")
        print("4. Calculadora")
        print("5. Positiu o Negatiu")
        print("6. Sortir")
        
        opcio = input("Tria una opció: ")
        if opcio == '1':
            calcul_de_area_cudrat()
        elif opcio == '2':
            ets_menor_o_major()
        elif opcio == '3':
            comparar_nums()
        elif opcio == '4':
            calculadora()
        elif opcio == '5':
            negatiu_o_positiu()
        elif opcio == '6':
            print("Gràcies. Adéu!")
            break
        else:
            print(" Opció no vàlida, torna-ho a provar.")


if __name__ == "__main__":
    main()