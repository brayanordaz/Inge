---------------------------------------------------------------------------------------------------------------Ejercicio 1


print("----------Programa que cada 5 números muestre el promedio, el valor minimo como maximo-----------")
print("-------------------------------------------------------------------------------------------------")
print("----------------------------Ingrese los 5 números enteros----------------------------------------")

a=int(input("Ingrese el primer número donde este sea el valor maximo: "))
b=int(input("Ingrese el segundo número: "))
c=int(input("Ingrese el tercer número: "))
d=int(input("Ingrese el cuarto número: "))
e=int(input("Ingrese el quinto número donde este sea el valor minimo: "))

Vmax=a
Vmin=e
P=(a+b+c+d+e)/5

print("El valor maximo de los números es: ",Vmax)
print("El valor minimo de los números es: ",Vmin)
print("El promedio de los números es: ",P)


---------------------------------------------------------------------------------------------------------------Ejercicio 2

print("----------Programa que pida un número entero del 0 al 9 y muestre su tabla de multiplicar-----------")
print("----------------------------------------------------------------------------------------------------")
print("-------------------------------------Ingrese un número del 0 al 9-----------------------------------")

Nm=int(input("Ingrese el número de la tabla que requiera saber: "))
Nm1=Nm*1
Nm2=Nm*2
Nm3=Nm*3
Nm4=Nm*4
Nm5=Nm*5
Nm6=Nm*6
Nm7=Nm*7
Nm8=Nm*8
Nm9=Nm*9
Nm10=Nm*10
Nm11=Nm*11
Nm12=Nm*12
Nm13=Nm*13
Nm14=Nm*14
Nm15=Nm*15

print(Nm,"x 1 = ",Nm1)
print(Nm,"x 2 = ",Nm2)
print(Nm,"x 3 = ",Nm3)
print(Nm,"x 4 = ",Nm4)
print(Nm,"x 5 = ",Nm5)
print(Nm,"x 6 = ",Nm6)
print(Nm,"x 7 = ",Nm7)
print(Nm,"x 8 = ",Nm8)
print(Nm,"x 9 = ",Nm9)
print(Nm,"x 10 = ",Nm10)
print(Nm,"x 11 = ",Nm11)
print(Nm,"x 12 = ",Nm12)
print(Nm,"x 13 = ",Nm13)
print(Nm,"x 14 = ",Nm14)
print(Nm,"x 15 = ",Nm15)

---------------------------------------------------------------------------------------------------------------Ejercicio 3


print("----------Programa que calcule la varianza de cinco números-----------")
print("----------------------------------------------------------------------")
print("----------------------Ingrese los 5 números---------------------------")

a=float(input("Ingrese el primer número: "))
b=float(input("Ingrese el segundo número: "))
c=float(input("Ingrese el tercer número: "))
d=float(input("Ingrese el cuarto número: "))
e=float(input("Ingrese el quinto número: "))

Media=(a+b+c+d+e)/5
Dif=(((a-Media)**2)+((b-Media)**2)+((c-Media)**2)+((d-Media)**2)+((e-Media)**2))
Var=Dif/5

print("La Varianza es: ", Var)


---------------------------------------------------------------------------------------------------------------Ejercicio 4


print("----------Traducir las expresiones matematicas y evaluarlas -----------")
print("-----------------------------------------------------------------------")
print("----------------------Expresiones traducidas---------------------------")

a=2+(3*(6/2))
b=(4+6)/(2+3)
c=(4/2)**5
d=(4/2)**(5+1)
e=(-3)**2
f=-(3**2)


print("Resultado de el A) es: ",a)
print("Resultado de el B) es: ",b)
print("Resultado de el C) es: ",c)
print("Resultado de el D) es: ",d)
print("Resultado de el E) es: ",e)
print("Resultado de el F) es: ",f)

---------------------------------------------------------------------------------------------------------------Ejercicio 5

print("----------Programa que evalue el polinomio en x = 1.1 -----------")
print("-----------------------------------------------------------------")
print("---------------------------Polinomio-----------------------------")

x=1.1
Polinomio=x**4+x**3+2*x**2-x

print("El resultado es: ",Polinomio)
