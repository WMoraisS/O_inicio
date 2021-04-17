function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fAno = document.getElementById("txtano")
    var res = document.querySelector("div#res")
    if (fAno.value.length == 0 || fAno.value > ano) {
        window.alert("Verifique os dados e tente novamente.")
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fAno.value)
        var genero = ''
        var img = document.createElement('img')
        var fetaria = ''
        
        img.setAttribute('id', 'foto')

        if (fsex[0].checked) {
            genero = 'homem'
            if (idade >= 0 && idade <10) {
                img.setAttribute('src', 'images/crianca-m.png')
                fetaria = 'menino'
            } else if (idade >= 10 && idade < 21) {
                img.setAttribute('src', 'images/jovem-m.png')
                fetaria = 'garoto'
            } else if (idade >=21 && idade <= 50) {
                img.setAttribute('src', 'images/adulto-m.png')
                fetaria = 'homem'
            } else {
                img.setAttribute('src', 'images/idoso-m.png')
                fetaria = 'senhor'
            }
        } else if (fsex[1].checked) {
            genero = 'mulher'
            if (idade >= 0 && idade <10) {
                img.setAttribute('src', 'images/crianca-f.png')
                fetaria = 'menina'
            } else if (idade >= 10 && idade < 21) {
                img.setAttribute('src', 'images/jovem-f.png')
                fetaria = 'garota'
            } else if (idade >=21 && idade < 50) {
                img.setAttribute('src', 'images/adulto-f.png')
                fetaria = 'mulher'
            } else {
                img.setAttribute('src', 'images/idoso-f.png')
                fetaria = 'senhora'
            }   
        }
        res.style.textAlign = "center"
        res.innerHTML = `Detectamos ${fetaria} com ${idade} anos.`
        res.appendChild(img)
    }

}
