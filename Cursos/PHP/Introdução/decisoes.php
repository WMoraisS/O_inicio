<?php

$idade = 17;
$numeroDePessoas = 2;

echo "Você só pode entra se tiver a partir de 18 anos." . PHP_EOL;

if ($idade >= 18) {
    echo "Você tem $idade anos." . PHP_EOL;
    echo 'Pode entrar sozinho.';

} elseif ($idade >= 16 && $numeroDePessoas > 1) { // && ou AND; || ou OR; != ou NOT
    echo "Você tem $idade, e está acompanhado. Pode entrar";

} else {
    echo "Você não pode entrar.";

}
