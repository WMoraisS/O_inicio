<?php

function exibeMsg(string $msg) {
    echo $msg . '<br>';
}

function sacar(array $conta,float $valor): array {

    if ($conta['saldo'] < $valor) {
        exibeMsg( "Você não pode sacar esse valor");
    } else {
        $conta['saldo'] -= $valor;
    }

    return $conta;
}

function depositar(array $conta, float $valor): array {

    $conta['saldo'] += $valor;
    return $conta;
}

function maiusculas(array &$conta) {           //    &   - Passagem por referência
    $conta['titular'] = strtoupper($conta['titular']);
}

function exibeConta(array $conta) {
    ['titular' => $titular, 'saldo' => $saldo] = $conta;
    echo "<li>Titular: $titular . Saldo: $saldo</li>";
}