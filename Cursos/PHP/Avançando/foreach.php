<?php

$contasCorrentes = [
    13254687145 => [
        'titular' => 'Joao',
        'saldo' => 1300
    ], 
    45268521456 => [
        'titular' => 'Maria',
        'saldo' => 4500
    ], 
    14568955423 => [
        'titular' => 'Jose',
        'saldo' => 5000
    ]
];

// ADICIONA DADOS A ARRAY ASSOCIATIVA
$contasCorrentes[12738402931] = [ 
    'titular' => 'Ana',
    'saldo' => 8400
];

foreach ($contasCorrentes as $cpf => $conta) {
    echo "$cpf " . $conta['titular'] . PHP_EOL;
}