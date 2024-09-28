BILLIFY ACME
Sistema de control de venta para micromercados de ACME SOFT


Contexto General


ACME Software tiene un producto de software llamado Billify el cual simplifica tu facturación y maximiza resultados. Este sistema se usa para el control de las ventas de los micromercados de la región. Este sistema de venta permite registrar información importante para las ventas como es los proveedores, productos, clientes, facturas, ventas; pero el sistema carece de un módulo de control de las ventas a través de informes. Para esto se le ha pedido que pueda implementar esta nueva opción en el software.


Su trabajo consiste en mostrar informes de las ventas a partir de los archivos maestros: productos.dat, clientes.dat y ventas.dat. 


El archivo productos.dat es un archivo de datos separados por punto y coma y la estructura de su encabezado es:

CODPROD;DESCPROD;VALORUNIT


Ejemplo de datos del archivo:

CODPROD;DESCPROD;VALORUNIT
001;Arroz 5kg;20000
002;Aceite vegetal 1L;12000
003;Azúcar 1kg;5500
004;Leche en polvo 500g;9500
005;Café molido 250g;15000


El archivo clientes.dat es un archivo de datos separados por punto y coma y la estructura de su encabezado es:

CODCLI;NOMBRE;TELEFONO


Ejemplo de datos del archivo:

CODCLI;NOMBRE;TELEFONO
001;Carlos Martínez;3104567890
002;Ana Gómez;3201234567
003;Pedro Rodríguez;3159876543
004;Laura Pérez;3112345678
005;Jorge Ramírez;3123456789


El archivo ventas.dat es un archivo de datos separados por punto y coma y la estructura de su encabezado es:

CODFACT;AÑO;MES;DIA;CODCLI;CODPROD;UNIDADESPROD;VALOR;VALORFACT


Ejemplo de datos del archivo:

CODFACT;AÑO;MES;DIA;CODCLI;CODPROD;UNIDADESPROD;VALOR;VALORFACT
001;2024;09;21;001;001;2;40000;66635
001;2024;09;21;001;003;3;16500;66635
002;2024;08;15;002;004;1;9500;25585
002;2024;08;15;002;002;1;12000;25585
003;2024;07;30;003;005;5;75000;89250
004;2024;09;10;004;003;4;22000;51135
004;2024;09;10;004;005;1;15000;51135
005;2024;06;25;005;001;1;20000;23800
006;2024;09;05;003;002;2;24000;35105
006;2024;09;05;003;004;1;9500;35105


Entre las características de este archivo se tienen:

·        La factura tiene un solo cliente.

·        Todos los registros de la factura tienen la fecha.

·        El cliente puede compra una o varias unidades de los productos

·        El cliente puede comprar uno o varios productos distintos.

·        Las unidades de un producto son mayores a cero.

·        El valor es la multiplicación del valor unitario del producto por las unidades.

·        El valor de la factura es la suma de los valores de cada registro de la factura agregando el valor del IVA 19%.


El módulo del sistema que usted se encargará de construir debe satisfacer los siguientes requerimientos: 

R1        Permitir imprimir una copia de una factura con los datos de ella. Al final discriminar el IVA del valor total de la factura.

R2      Imprimir un resumen de todas las facturas de un cliente de un mes solicitado. Este informe debe tener, el código y nombre del cliente, el número y nombre del mes; las facturas de dicho cliente en ese mes, el valor del IVA, el valor de la factura sin IVA y el valor de factura con IVA.

R3      Un diagrama de barras que muestre gráficamente un comparativo de los valores de las facturas de los meses de un año. Ejemplo tomando los datos anteriores:

 

====================
  FACTURACIÓN DEL 2024
====================
 
 MESES
-------------
06 ****
07 ****
08 ********************
09 ******************


R4       Dar un listado de productos comunes comprados entre dos clientes.


Adicionalmente, se deben hacer validaciones de errores y excepciones con el fin de evitar que el aplicativo se detengámoslos de forma inesperada.