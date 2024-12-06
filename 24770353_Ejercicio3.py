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
