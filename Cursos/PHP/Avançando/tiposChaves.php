<?php

$array = [
    1 => 'a',
    '1' => 'b', // a string é convertida para 1
    true => 'd' // TRUE é convertida para 1, FALSE para 0
];

foreach ($array as $item) {
    echo $item . PHP_EOL;
}

// https://www.php.net/manual/pt_BR/language.types.array.php