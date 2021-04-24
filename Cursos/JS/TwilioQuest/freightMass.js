var arr = ['cat', 'dog', 'bird', 'monkey', 'fish', 'elephant', 'frog', 'leopard']
var totalLength = calculateMass(arr)

function calculateMass(arr) {
    var total = 0
    arr.forEach(item => {
        total = total + item.length
    });

    return total
}

console.log('No vetor temos ' + totalLength + ' caracteres')