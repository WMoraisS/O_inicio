class Ducktipium {
    
    constructor(color) {
        this.color = color
        this.calibrationSequence = []
    }

    refract(cor, cor2) {
        
        if ((cor == 'red' || cor == 'blue') && (cor2 == 'blue' || cor2 == 'red')) {
            return 'purple'
        } else if ((cor == 'red' || cor == 'yellow') && (cor2 == 'yellow' || cor2 == 'red')) {
            return 'orange'
        } else {
            return 'green'
        }
    }
    calibrate(arr) {
        var i = 0
        var total = arr.forEach(item => {
            this.calibrationSequence[i] = arr[i] * 3
            i += 1
        });
        
        this.calibrationSequence = arr.sort()
    }
}

try {

    let cor = process.argv[2]
    let cor2 = process.argv[3]
    if ((cor.toLowerCase() != 'red') && (cor.toLowerCase() != 'blue') && (cor.toLowerCase() != 'yellow')) throw 'Escolha duas diferentes cores entre as três: RED, BLUE ou YELLOW';
    if (((cor2.toLowerCase() != 'red') && (cor2.toLowerCase() != 'blue') && (cor2.toLowerCase() != 'yellow')) || (cor2.toLowerCase() == cor.toLowerCase())) throw 'Escolha duas diferentes cores entre as três: RED, BLUE ou YELLOW';
    const cristal = new Ducktipium(cor)
    cristal.calibrate([3,5,1])
    console.log(cristal.color + " " + cor2)
    console.log(cristal.refract(cor, cor2))
    console.log(cristal.calibrationSequence)

} catch(erro) {
    console.log(erro)
};
