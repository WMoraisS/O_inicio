class Ducktypium {
    
    constructor(color) {
        if ((color.toLowerCase() != 'red') && (color.toLowerCase() != 'blue') && (color.toLowerCase() != 'yellow')) throw 'Escolha duas diferentes cores entre as três: RED, BLUE ou YELLOW';
        this.color = color
        this.calibrationSequence = []
    }

    refract(cor2) {
        
        if (this.color == cor2) {
            
        } else if ((this.color == 'red' || this.color == 'yellow') && (cor2 == 'yellow' || cor2 == 'red')) {
            this.color = 'orange'
        } else if ((this.color == 'red' || this.color == 'blue') && (cor2 == 'blue' || cor2 == 'red')) {
            this.color = 'purple'
            
        } else {
            this.color = 'green'
        }
        return this.color
    }
    
    calibrate(arr) {

        this.calibrationSequence = arr.sort()
        var i = 0
        arr.forEach(item => {
            this.calibrationSequence[i] = arr[i] * 3
            i += 1
        });
                
    }
}

try {
    
    let cor = process.argv[2]
    let cor2 = process.argv[3]
    const cristal = new Ducktypium(cor)
    cristal.calibrate([3,5,1])
    console.log(cristal.color + " " + cor2)
    console.log(cristal.refract(cor2))
    console.log(cristal.calibrationSequence)
    
} catch(erro) {
    console.log(erro)
};

