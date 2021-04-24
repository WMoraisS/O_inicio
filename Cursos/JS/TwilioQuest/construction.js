function construct(nome) {
    let robot = {
        name: nome,
        material: 'human',
        assemble: true,
        duration: 1000
    }

    return robot
}

var someone = construct('Elliot')
console.log('O nome é ' + someone.name)