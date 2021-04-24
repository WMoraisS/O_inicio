var arr = ['contraband', 'apples', 'cats', 'contraband', 'contraband', ]
var indexItens = scan(arr)

function scan(arr) {
    i = 0
    positions = []
    while (i <= arr.length) {
        if (arr[i] == 'contraband') {
            positions.push(i)
        }
        i += 1
    }


    return positions
}

console.log('"contraband" is location in positions: ' + indexItens)
