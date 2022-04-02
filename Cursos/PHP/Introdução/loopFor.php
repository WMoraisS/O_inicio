<?php

/* 
$cont = $cont + 1
$cont += 1
$cont++
*/

for ($cont = 1; $cont <= 15; $cont++) {
    if ($cont == 13) {
        continue; // 'continue' - pula para o próximo loop; 'break' - interrompe o loop
    } 
    echo "#$cont" . PHP_EOL;
    
}