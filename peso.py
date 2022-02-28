peso = float(input())
estatura = float(input())
masaCorporal = (peso / estatura**2)
if masaCorporal < 18.5:
    print('bajo peso')
elif masaCorporal <= 24.9:
    print('normal')
elif masaCorporal <= 29.9:
    print('sobrepeso')
else:
    print ("obeso")
control= float(22)
pesoideal=control*(estatura**2)
if  masaCorporal < 18.5:
    print("ganar ",round(pesoideal-peso,4))
if masaCorporal >25:
    print("perder ",round(peso-pesoideal,4))

print(pesoideal)