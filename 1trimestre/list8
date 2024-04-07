let lado1 = parseFloat(prompt('Digite o primeiro lado: '));
let lado2 = parseFloat(prompt('Digite o segundo lado: '));
let lado3 = parseFloat(prompt('Digite o terceiro lado: '));

if (lado1 <= 0 || lado2 <= 0 || lado3 <= 0) {
    console.log('Os valores dos lados devem ser maiores que zero.');
} else if (lado1 + lado2 > lado3 && lado1 + lado3 > lado2 && lado2 + lado3 > lado1) {
    if (lado1 === lado2 && lado1 === lado3) {
        console.log('Os valores podem formar um triângulo Equilátero.');
    } else if (lado1 === lado2 || lado1 === lado3 || lado2 === lado3) {
        console.log('Os valores podem formar um triângulo Isósceles.');
    } else {
        console.log('Os valores podem formar um triângulo Escaleno.');
    }
} else {
    console.log('Os valores não podem formar um triângulo.');
}
