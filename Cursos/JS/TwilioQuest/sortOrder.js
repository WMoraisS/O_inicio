var arg1 = process.argv[2]
var arg2 = process.argv[3]
var resp = ''

if (arg1.toLowerCase() < arg2.toLowerCase()) {
    resp = -1
} else if (arg1.toLowerCase() > arg2.toLowerCase()) {
    resp = 1
} else {
    resp = 0
}

console.log(resp)