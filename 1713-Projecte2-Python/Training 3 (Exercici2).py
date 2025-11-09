#Training 3 (Exercici2):
text1=int(input('Introdueix el primer numero que vols comparar: '))
text2=int(input('Introdueix el segon numero que vols comparar: '))
text3=int(input('Introdueix el tercer numero que vols comparar: '))

if text1 > text2 and text1 > text3 :
	print(text1, "es el major")
elif text2 >= text1 and text2 >= text3 :
	print(text2, "es el major")
elif text3 >= text1 and text3 >= text2 :
	print(text3, "es el major")