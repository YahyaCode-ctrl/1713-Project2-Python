#Training: Exercici 2: 
print(' la calculadura de Yahya Elhadri')
text1= input('Introdueix el primer numero: ')
text2= input('Introdueix el segon numero : ')
text3= input("Tria l'operacio que vols fer ( + , - , * , / ) :     ")
if text3 == '+' :
    print('Suma dels dos numeros    : ' , int(text1) + int(text2))
elif text3 == '-' :
    print('Resta dels numeros       : ' , int(text1) - int(text2))
elif text3 == '*' :
    print('Multiplicacio del numeros: ' , int(text1) * int(text2))
elif text3 == '/' :
    print('Divisio dels numeros     : ' , int(text1) / int(text2))
else :
    print('Operacio no valida')
    