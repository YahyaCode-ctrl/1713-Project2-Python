#Training 4 Exercici2 :
un_deu = False
print("--- Introdueix les notes (de 0 a 10). Escriu -1 per acabar ---")
while True:
    nota = int(input("Introdueix una nota: "))
    if nota == -1:
        break
    if nota == 10:
        un_deu = True
if un_deu == True:
    print(" --- Resultat: Hi ha hagut alguna nota que té un 10 ---")
else:
    print(" --- Resultat: No hi ha cap 10 ---")