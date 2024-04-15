let x = parseFloat(prompt("Digite um peso:"));
let y = parseFloat(prompt("Digite uma altura:"));

while (x < 0 || y < 0) {
    console.log("Erro, digite novamente.");
    x = parseFloat(prompt("Digite um peso:"));
    y = parseFloat(prompt("Digite uma altura:"));
}

let calculadora_de_imc = x / (y * y);

if (calculadora_de_imc > 0 && calculadora_de_imc < 18.5) { 
    console.log("O imc é:", calculadora_de_imc.toFixed(2));
    console.log("Abaixo do peso");
} else if (calculadora_de_imc >= 18.5 && calculadora_de_imc < 24.9) {
    console.log("O imc é:", calculadora_de_imc.toFixed(2));
    console.log("Peso normal");
} else if (calculadora_de_imc >= 25.0 && calculadora_de_imc < 29.9) {
    console.log("O imc é:", calculadora_de_imc.toFixed(2));
    console.log("Sobrepeso");
} else if (calculadora_de_imc >= 30.0 && calculadora_de_imc < 34.9) {
    console.log("O imc é:", calculadora_de_imc.toFixed(2));
    let w = calculadora_de_imc * 0.2;
    console.log("Obesidade grau 1, precisa perder:", w);
} else if (calculadora_de_imc >= 35.0 && calculadora_de_imc < 39.9) {
    console.log("O imc é:", calculadora_de_imc.toFixed(2));
    let p = calculadora_de_imc * 0.3;
    console.log("Obesidade grau 2 (severa), precisa perder:", p.toFixed(2));
} else {
    console.log("O imc é:", calculadora_de_imc.toFixed(2));
    let o = calculadora_de_imc * 0.4;
    console.log("Obesidade grau 3 (mórbida), precisa perder:", o.toFixed(2));
}
