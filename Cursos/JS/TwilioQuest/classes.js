class Materializer {
    
    constructor(target) {
        this.target = target
        this.activated = false
    }

    activate() {
        this.activated = true
    } 

    materialize() {
        var resp = ''
        if (this.activated == true) {
            return this.target
        }
    }
    
}

const robot = new Materializer('Elliot')
console.log(robot.activated)
robot.activate()
console.log(robot.activated)
console.log(robot.materialize())