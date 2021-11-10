// CÓDIGO SAP: document.getElementsByName("comp[ XXXXX ][composicao_codigo]")[0].value
// QUANTIDADE: document.getElementsByName("comp[ XXXXX ][composicao_qtd]")[0].value

var x = document.getElementsByClassName("list-group list-group-flush listaComponentes")[2].getElementsByClassName("row list-group-item")
var codSAP
var qtd
var table = ""
for (var i = 0; i < x.length; i++){
    var html = ""
    codSAP = x[i].getElementsByClassName("hide")[0].getElementsByTagName("input")[2].value
    qtd = x[i].getElementsByClassName("hide")[0].getElementsByTagName("input")[3].value
    html += '<table><tr><td>'+ codSAP + " " + qtd +'</td></tr></table>'
    table = table + html
}

if (document.getElementsByClassName('col-sm-12')[89].getElementsByTagName('b').text = "Lista técnica (Composição):") {
    
  
        //var local = document.getElementsByClassName("row")[234]
        // class="modal-backdrop fade in"    //   class="modal-open"
        var local = document.getElementsByClassName('col-sm-12')[89]
        local.innerHTML = local.innerHTML + table
        
}
