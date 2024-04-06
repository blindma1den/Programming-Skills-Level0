<?php 
  const USERNAME = "user123";
  const PASSWORD = "pass123";
  $registro;

  $liverpool = [
    "computerScience" => [["j","a"],["s","q"],["w","e"],["r","t"]],
    "medicine" => [["d","c"],["f","v"],["g","b"],["v","e"]],
    "marketing" => [["z","x"],["h","n"],["y","u"],["i","o"]],
    "arts" => [["p","l"],["j","k"],["i","m"],["n","d"]]
  ];

  $london = [
    "computerScience" => [["j","a"],["s","q"],["w","e"],["r","t"]],
    "medicine" => [["d","c"],["f","v"],["g","b"],["v","e"]],
    "marketing" => [["z","x"],["h","n"],["y","u"],["i","o"]],
    "arts" => [["p","l"],["j","k"],["i","m"],["n","d"]]
  ];

  $manchester = [
    "computerScience" => [["j","a"],["s","q"]],
    "medicine" => [["d","c"],["f","v"]],
    "marketing" => [["z","x"],["h","n"]],
    "arts" => [["p","l"],["j","k"]]
  ];

  // echo count($manchester["computerScience"]);


  function pedirDatos() {
    echo "Ingrese sus datos para la incripcion: \n";
    echo "\n";
    $nombre = readline("Ingrese su nombre: \n");
    $apellido = readline("Ingrese su apellido: \n");
    $programa = readline("Ingrese el programa que quiere estudiar: \n");
    $ciudad = readline("Ingrese la ciudad donde quiere estudiar (1:liverpool, 2:Manchester, 3:london): \n");

    return  [
      "nombre" => $nombre, 
      "apellido" => $apellido, 
      "programa" => $programa, 
      "ciudad" => $ciudad
    ];

  }

  function mostrarMenu() {
    global $registro;

    echo "Programas disponibles: \n";
    echo "\n";
    echo "[1] . Computer Science\n";
    echo "[2] . Medicine\n";
    echo "[3] . Marketing\n";
    echo "[4] . Arts\n";
    echo "[5] . Exit\n";

    $registro = pedirDatos();
  }

  function guardarRegistro() {
    global $registro;
    global $liverpool;
    global $manchester;
    global  $london;

    mostrarMenu();

    if($registro["ciudad"] == '1'){
      foreach($liverpool as $programa) {
        if(count($programa) < 5) {
          if($registro["programa"] == "1") {
            $liverpool[0][] = $registro;
            echo "Registro exitoso\n";
            guardarRegistro();
            break;
          }
          else if($registro["programa"] == "2") {
            $liverpool[1][] = $registro;
            echo "Registro exitoso\n";
            guardarRegistro();
            break;
          }
          else if($registro["programa"] == "3") {
            $liverpool[2][] = $registro;
            echo "Registro exitoso\n";
            guardarRegistro();
            break;
          }
          if($registro["programa"] == "4") {
            $liverpool[3][] = $registro;
            echo "Registro exitoso\n";
            guardarRegistro();
            break;
          }
        }
        else {
          echo "El programa se encuentra lleno";
          guardarRegistro();
        }
      }
    }
    else if($registro["ciudad"] == '2'){
      foreach($manchester as $programa) {
        if(count($programa) < 5) {
          if($registro["programa"] == "1") {
            $manchester[0][] = $registro;
            echo "Registro exitoso\n";
            guardarRegistro();
            break;
          }
          else if($registro["programa"] == "2") {
            $manchester[1][] = $registro;
            echo "Registro exitoso\n";
            guardarRegistro();
            break;
          }
          else if($registro["programa"] == "3") {
            $manchester[2][] = $registro;
            echo "Registro exitoso\n";
            guardarRegistro();
            break;
          }
          if($registro["programa"] == "4") {
            $manchester[3][] = $registro;
            echo "Registro exitoso\n";
            guardarRegistro();
            break;
          }
        }
        else {
          echo "El programa se encuentra lleno";
          guardarRegistro();
        }
      }
    }

    else if($registro["ciudad"] == '3'){
      foreach($london as $programa) {
        if(count($programa) < 5) {
          if($registro["programa"] == "1") {
            $london[0][] = $registro;
            echo "Registro exitoso\n";
            guardarRegistro();
            break;
          }
          else if($registro["programa"] == "2") {
            $london[1][] = $registro;
            echo "Registro exitoso\n";
            guardarRegistro();
            break;
          }
          else if($registro["programa"] == "3") {
            $london[2][] = $registro;
            echo "Registro exitoso\n";
            guardarRegistro();

            break;
          }
          if($registro["programa"] == "4") {
            $london[3][] = $registro;
            echo "Registro exitoso\n";
            guardarRegistro();
            break;
          }
        }
        else {
          echo "El programa se encuentra lleno";
          guardarRegistro();
        }
      }
    }
    else if($registro["programa"] == "5") {
      exit();
    }
    else {
      echo "Numero incorecto";
      guardarRegistro();
    }
  }

  function login() {
    $contador = 3;

    while($contador > 0) {
      $user = readline("Ingrese su usuario: ");
      $pass = readline("Ingrese su contraseña: ");

      if($user === USERNAME &&  $pass === PASSWORD){
        echo "Bienvenido";
        guardarRegistro();
        die("Gracias  por ingresar");
      }
      else {
        echo "Usuario o contraseña incorectos";
        $contador--;
        echo "Tiene $contador intentos mas";
      }
    }
  }

  login();
?>