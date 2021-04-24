
const num = process.argv[2]
let str = ''

if ((num % 3 === 0 || num % 5 === 0 ) == false) {
    str = String(num)
} else {
    if (num % 3 === 0) {
        str += 'Java'
    }

    if (num % 5 === 0) {
        str += 'Script'
    }
}

console.log(str)