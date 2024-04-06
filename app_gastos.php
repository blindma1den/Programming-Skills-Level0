<?php 

$sueldo = readline("Ingrese su sueldo: \n");

function listarGastos($medico, $hogar, $ocio, $ahorro, $educacion) {
  echo "\n"."------- Lista de gatos --------" . "\n";
  echo "Gastos medicos: ".$medico."\n";
  echo "Gastos de hogar: ".$hogar."\n" ;
  echo "Gastos de ocio: ".$ocio."\n" ;
  echo "Ahorros: ".$ahorro."\n" ;
  echo "Educacion: ".$educacion."\n";
}

function mostrarTotalGastado($medico, $hogar, $ocio, $educacion) {
  global  $sueldo;

  $total = $medico + $hogar + $ocio + $educacion;

  echo  "\n Total gastado: $total\n";

  if($total >= $sueldo){
    echo "Has gastado mucho dinero este mes debes hacer un replanteamiento de que es necesario y que no\n";
  } else{
    echo "Felicidades has reducido tus gastos\n";
  };
}

function registraGastos() {
  $medico = intval(readline("Ingrese sus gastos medicos: \n"));
  $hogar = intval(readline("Ingrese sus gastos del hogar: \n"));
  $ocio = intval(readline("Ingrese sus gastos de ocio: \n"));
  $ahorro = intval(readline("Ingrese lo que se ahorra al mes: \n"));
  $educacion = intval(readline("Ingrese  los costos educativos: \n"));

  listarGastos($medico, $hogar, $ocio, $ahorro, $educacion);
  mostrarTotalGastado($medico, $hogar, $ocio, $educacion);
}

registraGastos();



?>