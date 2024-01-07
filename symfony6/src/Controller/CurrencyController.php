<?php

namespace App\Controller;


use Symfony\Component\HttpFoundation\Request;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Attribute\AsController;
use Symfony\Component\Routing\Annotation\Route;

#[AsController]
class CurrencyController extends AbstractController
{
    #[Route('/', name: 'app_currency')]
    public function index(): Response
    {
        return $this->render('currency/index.html.twig', [
            'controller_name' => 'CurrencyController',
        ]);
    }

    #[Route('/api/change_money', name: 'change_money')]
    public function change_money(Request $request): \Symfony\Component\HttpFoundation\JsonResponse
    {

        $parameters = json_decode($request->getContent(), true);
       // echo $parameters['valor']; // will print 'user'

        $valor2 = 0;

        $moneda1 = $parameters['moneda1'];
        $moneda2 = $parameters['moneda2'];
        $valor1 = $parameters['valor'];

        //Tasas de cambio CLP
        $valueCLP_ARS = 0.90812;
        $valueCLP_EUR = 0.00102;
        $valueCLP_USD = 0.001117;
        $valueCLP_TRY = 0.03338;
        $valueCLP_GBP = 0.000883;

        //Tasas de cambio EUR
        $valueEUR_TRY = 32.58;
        $valueEUR_GBP = 0.862;
        $valueEUR_CLP = 972.23;
        $valueEUR_ARS = 885.9;
        $valueEUR_USD = 1.0918;

        //Tasas de cambio USD
        $valueUSD_CLP = 894.100;
        $valueUSD_ARS = 811.700;
        $valueUSD_EUR = 0.915;
        $valueUSD_TRY = 29.84;
        $valueUSD_GBP = 0.789;

        //Tasas de cambio TRY
        $valueTRY_GBP = 0.026;
        $valueTRY_CLP = 29.94;
        $valueTRY_ARS = 27.19;
        $valueTRY_USD = 0.0335;
        $valueTRY_EUR = 0.030;

        //Tasas de cambio GBP
        $valueGBP_EUR = 1.15;
        $valueGBP_USD = 1.26;
        $valueGBP_CLP = 1132.08;
        $valueGBP_ARS = 1028.25;
        $valueGBP_TRY = 37.79;

        //Tasas de cambio ARS
        $valueARS_USD = 0.00123;
        $valueARS_CLP = 1.10117;
        $valueARS_EUR = 0.001128;
        $valueARS_TRY = 0.0367;
        $valueARS_GBP = 0.00097;


        if ($moneda1 === $moneda2) {
            $valor2 = 1;
        }

        //CLP to --> other
        if ($moneda1 === "CLP" && $moneda2 === "ARS") {
            $valor2 = $valor1 * $valueCLP_ARS;
        }
        if ($moneda1 === "CLP" && $moneda2 === "EUR") {
            $valor2 = $valor1 * $valueCLP_EUR;
        }
        if ($moneda1 === "CLP" && $moneda2 === "USD") {
            $valor2 = $valor1 * $valueCLP_USD;
        }
        if ($moneda1 === "CLP" && $moneda2 === "TRY") {
            $valor2 = $valor1 * $valueCLP_TRY;
        }

        if ($moneda1 === "CLP" && $moneda2 === "GBP") {
            $valor2 = $valor1 * $valueCLP_GBP;
        }

//ARS  to --> other
        if ($moneda1 === "ARS" && $moneda2 === "CLP") {
            $valor2 = $valor1 * $valueARS_CLP;
        }
        if ($moneda1 === "ARS" && $moneda2 === "EUR") {
            $valor2 = $valor1 * $valueARS_EUR;
        }
        if ($moneda1 === "ARS" && $moneda2 === "USD") {
            $valor2 = $valor1 * $valueARS_USD;
        }
        if ($moneda1 === "ARS" && $moneda2 === "TRY") {
            $valor2 = $valor1 * $valueARS_TRY;
        }

        if ($moneda1 === "ARS" && $moneda2 === "GBP") {
            $valor2 = $valor1 * $valueARS_GBP;
        }

        //USD  to --> other
        if ($moneda1 === "USD" && $moneda2 === "CLP") {
            $valor2 = $valor1 * $valueUSD_CLP;
        }
        if ($moneda1 === "USD" && $moneda2 === "EUR") {
            $valor2 = $valor1 * $valueUSD_EUR;
        }
        if ($moneda1 === "USD" && $moneda2 === "TRY") {
            $valor2 = $valor1 * $valueUSD_TRY;
        }

        if ($moneda1 === "USD" && $moneda2 === "GBP") {
            $valor2 = $valor1 * $valueUSD_GBP;
        }

        //EUR  to --> other
        if ($moneda1 === "EUR" && $moneda2 === "CLP") {
            $valor2 = $valor1 * $valueEUR_CLP;
        }
        if ($moneda1 === "EUR" && $moneda2 === "USD") {
            $valor2 = $valor1 * $valueEUR_USD;
        }
        if ($moneda1 === "EUR" && $moneda2 === "TRY") {
            $valor2 = $valor1 * $valueEUR_TRY;
        }

        if ($moneda1 === "EUR" && $moneda2 === "GBP") {
            $valor2 = $valor1 * $valueEUR_GBP;
        }
        if ($moneda1 === "EUR" && $moneda2 === "ARS") {
            $valor2 = $valor1 * $valueEUR_ARS;
        }

        //TRY  to --> other
        if ($moneda1 === "TRY" && $moneda2 === "CLP") {
            $valor2 = $valor1 * $valueTRY_CLP;
        }
        if ($moneda1 === "TRY" && $moneda2 === "USD") {

            $valor2 = $valor1 * $valueTRY_USD;
        }
        if ($moneda1 === "TRY" && $moneda2 === "EUR") {
            $valor2 = $valor1 * $valueTRY_EUR;
        }

        if ($moneda1 === "TRY" && $moneda2 === "GBP") {
            $valor2 = $valor1 * $valueTRY_GBP;
        }
        if ($moneda1 === "TRY" && $moneda2 === "ARS") {
            $valor2 = $valor1 * $valueTRY_ARS;
        }

        //GBP  to --> other
        if ($moneda1 === "GBP" && $moneda2 === "CLP") {
            $valor2 = $valor1 * $valueGBP_CLP;
        }
        if ($moneda1 === "GBP" && $moneda2 === "USD") {
            $valor2 = $valor1 * $valueGBP_USD;
        }
        if ($moneda1 === "GBP" && $moneda2 === "EUR") {
            $valor2 = $valor1 * $valueGBP_EUR;
        }

        if ($moneda1 === "GBP" && $moneda2 === "TRY") {
            $valor2 = $valor1 * $valueGBP_TRY;
        }
        if ($moneda1 === "GBP" && $moneda2 === "ARS") {
            $valor2 = $valor1 * $valueGBP_ARS;
        }
//var_dump($valor2);
       return $this->json($valor2);


    }
    #[Route('/discount', name: 'discount')]
    public function withdraw_discount(int $valor2): int
    {
        $descuento = $valor2 / 100;
        $costo_a_pagar = $valor2 - $descuento;

        return $costo_a_pagar;

    }

}
