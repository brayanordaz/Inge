Algoritmo factorialparaelnumero5
	definir n, factorial como real 
	Definir procedimiemto  Como Caracter
	escribir "ingrese un numero" (natural) 
	leer n 
	Mientras  n<0 Hacer
		escribir "error:numero mal ingresado , ingrese un numero (natural) , (>=0)" 
		leer n 
	FinMientras
	factorial<-1
	procedimiento <-"" 
	si n=0 o n=1 Entonces //n<=1 
		escribir '--------------------factorial--------------------' 
		escribir n ,'!=',1
		Escribir '------------------------------------------------'
	sino 
		para i<-1 Hasta n Con Paso 1 Hacer
			factorial<-factorial *i 
			si i <> n Entonces
				procedimiento=procedimiento+ConvertirATexto(i)+' x ' 
			SiNo
				procedimiento=procedimiento+ConvertirATexto(i) 
				
			FinSi
			
		FinPara
		escribir'--------------------factorial--------------------' 
		escribir n , ' ! = ' , procedimiento, ' = ', factorial 
		escribir ' ------------------------------------------------- ' 
	
	FinSi
FinAlgoritmo
