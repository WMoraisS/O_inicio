<?php

$string = 'Testes de integração com PHP';

echo "Função normal: " . strlen($string) . PHP_EOL;
echo "MultiByte: " . mb_strlen($string) . PHP_EOL . PHP_EOL;

echo "Função normal: " . strtoupper($string) . PHP_EOL;
echo "MultiByte" . mb_strtoupper($string) . PHP_EOL;