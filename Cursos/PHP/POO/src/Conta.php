<?php

class Conta {
    public string $cpf;
    public string $nome;
    public float $saldo;
}

$primeiraConta = new Conta();
$primeiraConta->cpf = '454.884.666-44';
$primeiraConta->nome = 'João';
$primeiraConta->saldo = '200';

$atalhoPrimeiraConta = $primeiraConta; //cria uma nova referência para a $primeiraConta

var_dump($atalhoPrimeiraConta);
