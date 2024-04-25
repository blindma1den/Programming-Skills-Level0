# Quinto reto de Level 0

Este reto se basa en un sistema de finanzas sencillo, donde colocas un ingreso total general y luego empiezas a registrar egresos categorizados.

Los requerimientos son:
- Registrar los ingresos totales.
  - Aquí se registrar el total de dinero "percibido".
  - Puede ser un número flotante.
- Registrar los egresos.
  - Los egresos se registran uno por uno:
    - Indicando primero el monto y luego la categoría, donde ésta estará visible en una interfaz y el usuario lo seleccionará.
  - Dado que el registro de egresos se da uno por uno, este se hará en un ciclo `while`, donde hará `break` cuando el usuario lo decida.
- Evaluación.
  - El programa evalúa si los egresos superan los ingresos y muestra una juicio en base al análisis hecho.
- Estadísticas.
  - Aunque no es un requerimiento del reto, decidí mostrar unas estadísticas que con el tiempo (espero 😓) poder seguir aumentando.
    - La primera estadística es el **promedio de egresos por categorías**.
  - Interface
    - Solo línea de comando
  - Excepciones
    - El programa trata de salvaguardar el flujo mediante excepciones `try-except` y condicionales `ifelse`.

---
*pd: Quizás en un futuro cercano, cuando sepa cómo el programa pueda ejecutar pandas, matplotlib o seaborn sin que el usuario que clone esto deba tenerlo instalado en su sistema pueda visualizar las estadísticas, decida aumentar y mejorar este código. Queda pendiente...*