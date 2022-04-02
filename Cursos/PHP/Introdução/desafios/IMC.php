<?php

$altura = 1.70;
$peso = 65;

$imc = $peso / $altura ** 2;

echo "Seu IMC é de $imc. Você está ";

if ($imc < 18.5) {
    echo "abaixo";
} elseif ($imc <= 24.9) {
    echo "dentro";
} else {
    echo "acima";
}

echo " do recomendado.";