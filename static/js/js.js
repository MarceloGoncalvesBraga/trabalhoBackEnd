<
button > Aperte - me < /button>
var button = document.querySelector('button');

button.onclick = function() {
    var titulo = prompt('Qual é o seu titulo?');
    alert('Olá ' + titulo + ', é um prazer te ver!');
}
var meutituloArray = ['Chris', 'Bob', 'Jim'];
var meuNumeroArray = [10, 15, 40];
meutituloArray[0]; // deve retornar 'Chris'
meuNumeroArray[2]; // deve retornar 40
var cachorro = { titulo: 'Totó', raca: 'Dálmata' };
cachorro.titulo