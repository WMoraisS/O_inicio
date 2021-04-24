var arr = ['um', 'Dois', 'Três']
const num = 2

getFirstAmountSorted(arr, num)

function getFirstAmountSorted(arr, num) {

    res = arr.sort()
    retorno = res.slice(0, num)
    console.log(retorno)
    
    return retorno
    
}

