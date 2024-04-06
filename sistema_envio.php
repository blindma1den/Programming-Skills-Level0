<?php 

const USERNAME = "user123";
const PASSWORD = "pass123";
// $paquete;

function menu() {
  echo "\n\nMenu: \n";
  echo "[1] - Enviar paquete\n";
  echo "[2] - Salir\n";
  echo "\n";
}

function calcularPrecio($peso) {
  $precio = $peso * 2;
  return $precio;
}

function infoPaquete($remitente, $destinatario, $peso){
  $pack =  [
    "remitente" => $remitente,
    "destinatario" => $destinatario,
    "peso" => $peso,
    "codigo" => rand(0,100)
  ];

  return $pack;
}

function datosPaquete() {
  global $paquete;

  $remitente = readline("Ingrese el nombre del remitente: \n");
  $destinatario = readline("Ingrese el nombre del destinatario: \n");
  $peso = readline("Ingrese el peso en kg: \n");
  $codigo = rand(0,99);
  
  echo "El monto a pagar es $".calcularPrecio($peso)."\n";
}

// function mostrarInfoPaquete(){

//   global $paquete;

//   foreach($paquete as  $key => $value) {
//     echo  "$key : $value \n";
//   }
// }

// mostrarInfoPaquete();



function escogerOpcion() {
  global $paquete;
  menu();

  $respuesta = readline("Que accion desea  realizar? ");
  if ($respuesta == '1'){

    datosPaquete();
    // mostrarInfoPaquete($paquete);    

    $masAcciones = readline("Quiere realizar otra operacion: (S/N): ");

    if($masAcciones === "S" || $masAcciones === "s") {
      escogerOpcion();
    } 
    else if($masAcciones === "n" || $masAcciones === "N") {
      exit();
    }
    else {
      echo "Opción no valida. Por favor ingrese S o N.\n\n";
      escogerOpcion();
    }

  } 
  elseif($respuesta == '2'){
    exit;
  }
  else{
    echo "Opcion no valida. Por favor, intente nuevamente.\n";
    sleep(2);
    escogerOpcion();
  }

}

function login() {
  $contador = 3;

  while($contador > 0) {
    $user = readline("Ingrese su usuario: \n");
    $pass = readline("Ingrese su contraseña: \n");

    if($user === USERNAME &&  $pass === PASSWORD){
      echo "Acceso permitido\n";
      escogerOpcion();
      break;  
    }
    else{
      echo "Usuario o contraseña incorrecta, intentelo nuevamente.\n";
      $contador--;
      echo "Intentos restantes : {$contador}\n\n";
    }

  }
}

login();

?>