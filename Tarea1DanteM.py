"DANTE.MENDOZA"
vector = [3, 5, 8, 9, 10, 22, 45, 500, 900, 4253]
puntero = 0
vectorLen = len(vector)
encontrado = False
numero = int(input("Ingresar el dato que desea buscar: "))
while not(encontrado) and puntero <= vectorLen:
	mitad = int((puntero+vectorLen) / 2)
	if numero == vector[mitad]:
		encontrado = True
	elif numero < vector[mitad]:
		vectorLen = mitad - 1
	else:
		puntero = mitad + 1
if(encontrado):
	print("El dato se encuentra en la posicion ", str(mitad))
	print(vector)
else:
	print("El dato no se encontro")