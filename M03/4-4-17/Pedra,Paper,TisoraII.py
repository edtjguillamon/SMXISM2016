#coding utf-8-*-
#pedra paper tisora II 

J1=num%7 
J2=num%5
Sortir=False
While (Sortir==False)
	print "pedra, paper, tisora" 
	
	if (J1==0 or J1==1):
		print "Tisora"
		
	if (J1==2 or J1==3):
		print "Pedra"
		
	if (J1==4 or J1==5):
		print "Papel"
		
	if (J1==6):
		print "Pedra"
	
	if (J2==0 or J2==1 or J2==2):
		print "Papel"
		
	if (J2==3):
		print "Tisora"
		
	if (J2==4):
		print "Pedra"
		
	if (J1==57 or J2==57):
		Sortir==True
		

	
