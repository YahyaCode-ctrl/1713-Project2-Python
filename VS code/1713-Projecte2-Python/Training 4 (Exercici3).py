#Training 4 Exercici3 :
un_negatiu = False
print(" --- Escriu 10 nombres enters ---")
for i in range(10):
    numero = int(input(f"Introdueix el número {i + 1}: "))
    if numero < 0: 
        un_negatiu = True
if un_negatiu == True:
    print(" --- Resultat: hi havia almenys un nombre negatiu ---")
else:
    print(" --- Resultat: no hi ha cap nombre negatiu ---")