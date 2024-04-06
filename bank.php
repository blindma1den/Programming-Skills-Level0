<?php 

define("USERNAME","user123");
define("PASSWORD", "pass123");
$balance = 2000;

function deposito($cantidad) {
  global $balance;
  $balance += $cantidad;
  echo "Operacion exitosa.\n";
}

function  retiro($cantidad){
  global $balance;
  if($cantidad > $balance) {
    echo "La cantidad  a retirar es mayor al saldo disponible.\n";
  } else{
  	$balance -= $cantidad;
  	echo "Retiro realizado con exito.\n";
  }
}

function consultaSaldo() {
  global $balance;
  return $balance;
}

function transferencia($cuenta_destino, $cantidad) {
  global  $balance;
  if($cantidad > $balance) {
    echo "La cantidad a tranferir supera su saldo\n";
  }else{
    echo "Transferencia realizada correctamente\n";
    $balance -= $cantidad;
  }
}

function operaciones_bancarias() {
  echo "\n";

  echo "Indique que operacion desea hacer mediante  el siguiente menu: " . "\n";

  echo "\n";

  echo 1 . " Depositar en la cuenta \n";
  echo 2 . " Retirar dinero de la cuenta \n";
  echo 3 . " Consultar saldo actual \n";
  echo 4 . " Realizar una transferencia \n";
  echo 5 . " Salir \n";

  echo "\n";

  $opcion=readline("Seleccione su opción: ");
  
  switch ($opcion) {
    case 1:
      $dinero = readline("Ingrese la cantidad a depositar: ");
      deposito($dinero);
      operaciones_bancarias();
      break;
    case 2:
      $retiro = readline("Ingrese la cantidad a retirar: ");
      retiro($retiro);
      operaciones_bancarias();
      break;
    case 3:
      echo "Su saldo es: ". consultaSaldo() . "\n";
      operaciones_bancarias();
      break;
    case 4:
      $numCuentaDestino = readline("Ingrese el número de cuenta destino: ");
      $monto = readline("Ingrese la cantidad a transferir: ");
      transferencia($numCuentaDestino, $monto);
      operaciones_bancarias();
      break;
    case 5:
      exit();
      break;
    default:
      echo "Opción no válida. Por favor, intente nuevamente." . "\n\n";
      operaciones_bancarias();
  }
}

function login() {
  $intentos = 3;
  
  while($intentos > 0) {
    $user = readline("Ingrese su usuario: ");
    $pass = readline("Ingrese su contraseña: ");

    if($user === USERNAME &&  $pass === PASSWORD){
      echo "Acceso permitido\n";
      operaciones_bancarias();
    }
    else{
      echo "Usuario o contraseña incorrecta.\n";
      $intentos--;
      echo "Intentos restantes: ". $intentos. "\n";
    }
  }

  die("Numero de intentos superados, Intentelo mas tarde");
}

login();

?>