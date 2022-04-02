<?php
// ARRAY ASSOCIATIVO
$conta1 = [
    'titular' => 'Joao',
    'saldo' => 1300
];
$conta2 = [
    'titular' => 'Maria',
    'saldo' => 4500
];
$conta3 = [
    'titular' => 'Jose',
    'saldo' => 5000
];

$contasCorrentes = [$conta1, $conta2, $conta3];

for ($i = 0; $i < count($contasCorrentes); $i++) {
    echo $contasCorrentes[$i]['titular'] . PHP_EOL;
}
