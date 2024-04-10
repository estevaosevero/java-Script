x = float(input("Digite um peso:"))
y = float(input("Digite uma altura:"))

calculadora_de_imc = x/(y*y)

if x < 0 or y < 0:
    print("Erro, númeração não válida")
elif calculadora_de_imc > 0 and calculadora_de_imc < 18.5: 
    print( "O imc é:",calculadora_de_imc)
    print("Abaixo do peso")
elif calculadora_de_imc > 18.5 and calculadora_de_imc < 24.9:
    print( "O imc é:",calculadora_de_imc)
    print("peso normal")
elif calculadora_de_imc > 25.0 and calculadora_de_imc < 29.9:
    print( "O imc é:",calculadora_de_imc)
    print("Sobrepeso")
elif calculadora_de_imc > 30.0 and calculadora_de_imc < 34.9:
    print( "O imc é:",calculadora_de_imc)
    w = calculadora_de_imc * 0.2
    print("Obesidade grau 1, precisa perder:",w)
elif calculadora_de_imc > 35.0 and calculadora_de_imc < 39.9:
    print( "O imc é:",calculadora_de_imc)
    p = calculadora_de_imc * 0.3
    print("Obesidade grau 2 (severa), precisa perder:",p)
else:
    print( "O imc é:",calculadora_de_imc)
    o = calculadora_de_imc *0.4
    print(f"Obesidade grau 3 (mórbida), precisa perder:",o)
