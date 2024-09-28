productos = './app_data/productos.dat'
clientes = './app_data/clientes.dat'
ventas = './app_data/ventas.dat'


tabla ="""
+----------------------------------------------------------------+
| 1. Copia de la factura con todos sus datos                     |
+----------------------------------------------------------------+
| 2. Resumen de todas las facturas de un mes                     |
+----------------------------------------------------------------+
| 3. Estudiantes que no han faltado a ningún módulo durante      |
|    un mes                                                      |
+----------------------------------------------------------------+
| 4. Diagrama de barras de los meses del año                     |
+----------------------------------------------------------------+"""

def leer_productos(archivo=productos):

    with open(archivo) as file:
        data = file.readlines()

    lineas_archivo = [x.strip() for x in data[1:]]
    codigos = []
    for indice in range(len(lineas_archivo)):
        codigos.append(lineas_archivo[indice].split(";")[0])

    lineas_archivo = [item.split(";") for item in lineas_archivo]

    contenido = dict.fromkeys(codigos)


    for key in contenido:
        contenido[key] = {"DESCPROD": None, "VALORUNIT": None}

    indice = 0
    for linea in lineas_archivo:
        contenido[codigos[indice]]["DESCPROD"] = linea[1]
        contenido[codigos[indice]]["VALORUNIT"] = linea[2]
        indice += 1
    
    return contenido


def leer_clientes(archivo=clientes):

    with open(archivo) as file:
        data = file.readlines()

    lineas_archivo = [x.strip() for x in data[1:]]
    codigos = []
    for indice in range(len(lineas_archivo)):
        codigos.append(lineas_archivo[indice].split(";")[0])

    lineas_archivo = [item.split(";") for item in lineas_archivo]

    contenido = dict.fromkeys(codigos)


    for key in contenido:
        contenido[key] = {"NOMBRE": None, "TELEFONO": None}

    indice = 0
    for linea in lineas_archivo:
        contenido[codigos[indice]]["NOMBRE"] = linea[1]
        contenido[codigos[indice]]["TELEFONO"] = linea[2]
        indice += 1
    
    return contenido


ventas = './app_data/ventas.dat'


def leer_ventas(archivo=ventas):

    with open(archivo) as file:
        data = file.readlines()

    lineas_archivo = [x.strip() for x in data[1:]]
    codigos = []
    for indice in range(len(lineas_archivo)):
        cod = lineas_archivo[indice].split(";")[0]
        if cod not in codigos:
            codigos.append(cod) 
    

    lineas_archivo = [item.split(";") for item in lineas_archivo]

    contenido = dict.fromkeys(codigos)


    for key in contenido:
        contenido[key] = {
            "AÑO": None, 
            "MES": None,
            "DIA": None,
            "CODCLI": None,
            "PRODUCTOS": {
                "CODPROD": None,
                "UNIDADESPROD": None,
                "VALOR": None
                },
            "VALORFACT": None
            }
    
    return contenido


def valor(factura, archivo=ventas):
    
    with open(archivo) as file:
        data = file.readlines()

    lineas_archivo = [x.strip() for x in data[1:]]
    
    valor = 0
    for linea in lineas_archivo:
        if linea.split(";")[0] == factura:
            valor += int(linea.split(";")[7])
    

    return valor
        
    

def obtener_resumen(info_clientes, archivo=ventas):
    while True:
        try:
            codigo_cliente = input("Ingrese el codigo de cliente\n>>> ").strip()
            mes_deseado = input("Ingrese el mes que desea consultar\n>>> ").strip()
            if codigo_cliente.lower() == 'e' or mes_deseado == 'e':
                break
            elif not (codigo_cliente.isdigit() and mes_deseado.isdigit()):
                print("Los codigos solo contienen numeros")
                continue             
            meses = {
                "01": "ENERO",
                "02": "FEBRERO", 
                "03": "MARZO",
                "04": "ABRIL",
                "05": "MAYO",
                "06": "JUNIO",
                "07": "JULIO",
                "08": "AGOSTO",
                "09": "SEPTIEMBRE",
                "10": "OCTUBRE",
                "11": "NOVIEMBRE",
                "12": "DICIEMBRE"
                }

            with open(archivo) as file:
                data = file.readlines()

            lineas_a_calcular = []
            lineas_archivo = [x.strip() for x in data[1:]]
            for linea in lineas_archivo:
                linea = linea.split(";")
                if codigo_cliente == linea[4] and mes_deseado == linea[2]:
                    lineas_a_calcular.append(linea)

            facturas_del_mes = []
            for linea in lineas_a_calcular:
                if linea[0] not in facturas_del_mes:
                    facturas_del_mes.append(linea[0])

            print(f"CODIGO DE CLIENTE: {codigo_cliente}\n")
            print(f"NOMBRE DEL CLIENTE: {info_clientes[codigo_cliente]['NOMBRE']}")
            print(f"MES {meses[mes_deseado]}, NUMERO {linea[2]}")
            print("El cliente tiene registradas las siguientes facturas")
            for factura in facturas_del_mes:
                print(f"Factura codigo {factura} con valor de IVA {round(valor(factura)) * 0.19} pesos.\nEl valor de la factura sin IVA es de {valor(factura) - round(valor(factura)) * 0.19} y su valor con IVA es de {round(valor(factura) * 1.19)}")

            print("\nPresione cualquier tecla para volver")
            input()
        except (ValueError, KeyError):
            print("Dato invalido\nPresione Enter para continuar")
            input()
            continue





def main():  

    data_productos = leer_productos()
    data_clientes = leer_clientes()
    data_ventas = leer_ventas()
    print(tabla)
    while True:
        try:
            print("Para salir escriba 'e'\n\n")
            
            print("Ingrese la opcion deseada\n>>> ", end='')
            respuesta = input().strip()
            if respuesta.lower() == 'e':
                break
            match respuesta:
                case '1':
                    pass
                case '2':
                    pass
                case '3':
                    obtener_resumen(data_clientes)
                
            
        except ValueError:
            print("Ha ingresado un dato invalido")
            continue
        else:
            pass


if __name__ == "__main__":
    main()