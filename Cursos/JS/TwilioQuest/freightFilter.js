var arr1 = ['Dog', 'Cat', 'Leon', 'Bear', 'Monkey', 'Dog', 'Dino',]
var arr2 = 'Dog'
var fil = scanAndFilter(arr1, arr2)


function scanAndFilter(arr1, arr2) {
    i = 0
    indexs = arr1.length
    while (i <= indexs) {
        if (arr1[i] == arr2) {
            arr1.splice(i, 1)
        }
        i += 1
    }
    return arr1
}

console.log('O elemento ' + arr2 + ' foi removido da lista que ficou assim: ' + fil)