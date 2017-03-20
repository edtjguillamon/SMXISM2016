#Exercici bucle python 
opcio = int(input("Selecciona una opcio\n"))

while (opc >0 and opc <5):

		x = int(input("Escriu un numero\n"))

		y = int(input("Escriu un altre numero\n"))

	if (opcio==1):
		print "La suma dona:", x+y

			opcio = int(input("Selecciona una opcio\n"))

	elif(opcio==2):

		print "La resta dona:",x-y

			opcio = int(input("Selecciona una opcio\n"))

	elif(opcio==3):

		print "La multiplicació dona:",x*y

			opcio = int(input("Selecciona una opcio\n"))
           
	elif(opc==4):

        try:

		print "La divisio es:", x/y

            opcio = int(input("Selecciona una opcio\n"))
