var nilai = 89;

if (nilai >90){
    document.write("nilai A")
} else if (nilai > 80 && nilai < 90){
    grade ="B"
} else if (nilai > 74 && nilai < 81){
    grade = "C"
} else{
    grade = "D"
}

document.write("nilai" + nilai + " masuk grade " + grade)