function compararNumeros(a, b) {
    return a - b;
}

function geraNumeros(num) {

    let arr = new Array();
    while (arr.length < num){
        let num = Math.round(Math.random() * 100)
        if(!arr.includes(num)){
            arr.push(num)
        }

    }
    arr = arr.sort(compararNumeros)
    return arr
}

console.log(geraNumeros(50))


