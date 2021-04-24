arg = process.argv[2];
num = Number(arg)
if (num == 0 ) {
    console.log('alive')
} else if (num == 1) {
    console.log('flowering')
} else if (num == 2) {
    console.log('shedding')
} else {
    console.log('other')
}