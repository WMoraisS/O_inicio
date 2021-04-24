
var arr = ['Um', 'Dois', 'Três','contraband', 'contraband', 'contraband']
var numItens = scan(arr)

function scan(arr) {
    contrabandCount = 0
    i = 0
    while (i <= arr.length) {        
        if (arr[i] == 'contraband') {
            contrabandCount += 1
        }
        i += 1
    }
    console.log(arr.length)

    return contrabandCount
}

numItens = Number(contrabandCount)
console.log('Number of "contraband": ' + numItens)