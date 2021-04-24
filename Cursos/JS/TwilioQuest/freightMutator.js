var carga = ['apples', 'ray guns', 'oranges', ]
var itensMutantes = mutate(carga)

function mutate(carga) {
    
    var arr = carga.map(item => item.toUpperCase())

    return arr
}

console.log('Carga mutante: ' + itensMutantes)
