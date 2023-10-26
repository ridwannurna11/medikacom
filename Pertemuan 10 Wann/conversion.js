var angkaString = '42';
// merubah string menjadi integer
var angkaInteger = parseInt(angkaString);
// merubah string menjadi float(desimal)
var angkaFloat = parseFloat(angkaString);

document.write("<h3>Conversion</h3>");
document.write("String: " + angkaString + "<br>");
document.write("Integer: " + angkaInteger + "<br>");
document.write("Float: " + angkaFloat + "<br>");

//Coercion (implicit type conversion)
var angka = 10;
var string = "30";
var hasil = angka + string;

document.write("<h3>Coercion</h3>");
document.write("Angka: " + angka + "<br>");
document.write("String: " + string + "<br>");
document.write("hasil: " + hasil + "<br>");

var boolean = true;
var number = 42;
var result = boolean + number
document.write("Boolean: " + boolean + "<br>");
document.write("Number: " + number + "<br>");
document.write("Result: " + result + "<br>");