class TargetingSolution {

    constructor(config) {
        this.coord = config
    }

    target() {
        return `(${this.coord.x}, ${this.coord.y}, ${this.coord.z})`
    }
    
}

const sln = new TargetingSolution({
    x: 45,
    y: 12,
    z: -1
});

console.log(sln.target())
