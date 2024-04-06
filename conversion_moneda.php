<?php
// Definir tasas de cambio y límites
$tasas = array(
    'CLP' => array('ARS' => 0.66, 'USD' => 0.0013, 'EUR' => 0.0011, 'TRY' => 0.011, 'GBP' => 0.0009),
    'ARS' => array('CLP' => 1.51, 'USD' => 0.020, 'EUR' => 0.017, 'TRY' => 0.18, 'GBP' => 0.015),
    'USD' => array('CLP' => 784.62, 'ARS' => 49.83, 'EUR' => 0.85, 'TRY' => 8.88, 'GBP' => 0.72),
    'EUR' => array('CLP' => 889.64, 'ARS' => 58.26, 'USD' => 1.18, 'TRY' => 10.44, 'GBP' => 0.85),
    'TRY' => array('CLP' => 90.90, 'ARS' => 5.52, 'USD' => 0.11, 'EUR' => 0.096, 'GBP' => 0.082),
    'GBP' => array('CLP' => 1121.54, 'ARS' => 67.15, 'USD' => 1.39, 'EUR' => 1.18, 'TRY' => 12.20)
);
$lim_min = array('CLP' => 1000, 'ARS' => 100, 'USD' => 10, 'EUR' => 10, 'TRY' => 50, 'GBP' => 10);
$lim_max = array('CLP' => 1000000, 'ARS' => 10000, 'USD' => 1000, 'EUR' => 1000, 'TRY' => 5000, 'GBP' => 1000);
$comision = 0.01;

function convertir($cantidad, $moneda_origen, $moneda_destino) {
    global $tasas, $lim_min, $lim_max;

    if ($cantidad < $lim_min[$moneda_origen] || $cantidad > $lim_max[$moneda_origen]) {
        echo "Cantidad fuera de límites.\n";
        return;
    }

    if ($moneda_origen === $moneda_destino) {
        echo "Las monedas son iguales. No es necesario convertir.\n";
        return $cantidad;
    }

    $tasa_cambio = $tasas[$moneda_origen][$moneda_destino];
    $cantidad_convertida = $cantidad * $tasa_cambio;

    if ($cantidad_convertida > $lim_max[$moneda_destino]) {
        echo "Cantidad convertida supera el límite máximo.\n";
        return;
    }

    return $cantidad_convertida;
}

function ejecutar() {
    global $tasas, $comision;

    while (true) {
        echo "\nBienvenido al Conversor de Divisas\n";
        echo "1. Convertir divisas\n";
        echo "2. Salir\n";
        $opcion = readline("Seleccione una opción: ");

        if ($opcion === "1") {
            $moneda_origen = strtoupper(readline("Ingrese su moneda inicial (CLP, ARS, USD, EUR, TRY, GBP): "));
            $moneda_destino = strtoupper(readline("Ingrese la moneda a la que quiere cambiar: "));

            if (!isset($tasas[$moneda_origen]) || !isset($tasas[$moneda_destino])) {
                echo "Moneda no válida.\n";
                continue;
            }

            $cantidad = floatval(readline("Ingrese la cantidad a convertir: "));

            if ($cantidad <= 0 || !is_numeric($cantidad)) {
                echo "Cantidad no válida.\n";
                continue;
            }

            $retirar_fondos = strtolower(readline("¿Desea retirar los fondos? (Sí/No): "));
            if ($retirar_fondos === 'sí' || $retirar_fondos === 'si') {
                $cantidad -= $cantidad * $comision;
                echo "Se aplicó una comisión del " . ($comision * 100) . "%\n";
                echo "Recibirá $cantidad $moneda_destino\n";
            } elseif ($retirar_fondos === 'no') {
                $resultado = convertir($cantidad, $moneda_origen, $moneda_destino);
                if ($resultado !== null) {
                    echo "Recibirá $resultado $moneda_destino\n";
                }
            } else {
                echo "Opción no válida.\n";
            }

        } elseif ($opcion === "2") {
            echo "¡Hasta luego!\n";
            break;
        } else {
            echo "Opción no válida. Por favor, seleccione 1 o 2.\n";
        }
    }
}

ejecutar();
?>
