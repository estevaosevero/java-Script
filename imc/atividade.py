x = float(input("Digite um peso:"))
y = float(input("Digite uma altura:"))

calculadora_de_imc = x/(y*y)
print( "O imc é:",calculadora_de_imc)
 
if calculadora_de_imc < 18.5:
    print("Abaixo do peso")
elif calculadora_de_imc > 18.5 and calculadora_de_imc < 24.9:
    print("peso normal")
elif calculadora_de_imc > 25.0 and calculadora_de_imc < 29.9:
    print("Sobrepeso")
elif calculadora_de_imc > 30.0 and calculadora_de_imc < 34.9:
    print("Obesidade grau 1")
elif calculadora_de_imc > 35.0 and calculadora_de_imc < 39.9:
    print("Obesidade grau 2 (severa)")
else:
    print("Obesidade grau 3 (mórbida)")


