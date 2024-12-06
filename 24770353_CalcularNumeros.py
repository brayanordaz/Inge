print("--------Calcular el Interés-------")

c=-1
i=0
m=0

while (c<0)or(i<=0)or(i>=100)or(m<=0):

    print("Introduce el capital, interés y el tiempo en años: ")
    c=int(input("Capital: "))
    i=int(input("Interés: "))
    m=int(input("Años:    "))
    for i in range (m):
          c=c*(1+i/100)
    print("Tienes ",c," de capital acumulado")