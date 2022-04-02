<?php

require_once 'functions.php';

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

$contasCorrentes[13254687145] = sacar($contasCorrentes[13254687145], 500);
$contasCorrentes[13254687145] = depositar($contasCorrentes[13254687145], 500);
maiusculas($contasCorrentes[13254687145]);

unset($contasCorrentes[13254687145]); // unset - deleta variáveis/array

echo "<ul>";
foreach ($contasCorrentes as $cpf => $conta) {
    ['titular' => $titular, 'saldo' => $saldo] = $conta; // ou list('titular' => $titular, 'saldo' => $saldo) = $conta;
    exibeConta($conta);
}

echo "</ul>";
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
  <h1>Contas correntes</h1>  

  <dl>
    <?php foreach ($contasCorrentes as $cpf => $conta) { ?>
    <dt>
        <h3><?= $conta['titular']; ?> - <?php echo $cpf; ?></h3>
    </dt>
    <dd>
        Saldo: R$ <?= number_format($conta['saldo'],2); ?>
    </dd>
    <?php } ?>
  </dl>
</body>
</html>

