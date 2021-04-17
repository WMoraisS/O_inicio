function carregar() {

    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('img')
    var data = new Date()
    var hora = data.getHours()
    hora = 15

    msg.innerHTML = `Agora são ${hora} horas`
    if (hora >= 0 && hora < 12) {
        // dia
        img.src = 'images/foto-manha.png'
        document.body.style.background = '#EFCEA8'
    } else if (hora >= 12 && hora < 18) {
        // tarde
        img.src = 'images/foto-tarde.png'
        document.body.style.background = '#EA6C00'
    } else {
        // noite
        img.src = 'images/foto-noite.png'
        document.body.style.background = '#7A7B7E'
    }

}