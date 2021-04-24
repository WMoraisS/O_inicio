

var elem1 = process.argv[2]
var elem2 = process.argv[3]
var elem3 = process.argv[4]

var arr = [elem1, elem2, elem3]

addFirstToLast(arr)

function addFirstToLast(arr) {
    let firstToLast = '';

    if (arr.length > 0) {
        firstToLast = arr[0] + arr[arr.length - 1]
    }
    
    return firstToLast
}