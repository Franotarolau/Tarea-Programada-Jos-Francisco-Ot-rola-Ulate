#Versión: 3.14.3
#Elaborado por: José Francisco Otárola Ulate y Ismael Torres
#Fecha de inicio: 1/5/26 3:16 PM
#Fecha de ultimo cambio: 13/5/26 11:20 PM
def cargarArchivo(ptokens):
    """
    La funcion de esta definición es cargar el archivo inicial donde se van a hacer todos los cambios
    Entradas: ptokens (list): Lista de tuplas (clave, valor) donde se almacenan los tokens. 
    Salidas:list: Lista actualizada de tokens después de leer el archivo.
    """
    nombreArchivo= input("Digite el nombre de su archivo: ").strip ()
    separador = input("Seleccione su separador('->', '=' o ','']'): ").strip ()

    if separador not in ["->", "=",  ","]:
        print ("Separador inválido. Seleccione '='', '->'' o ','")
        separador = input("Ingrese tipo de separador: ").strip()
    
    try:
        with open (nombreArchivo, "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if separador in linea:
                    partes = linea.split(separador)
                    if len(partes) == 2:
                        clave = partes[0].strip()
                        valor = partes[1].strip()
                        ptokens = actualizarToken(ptokens, clave, valor)

        print("Archivo cargado correctamente.\n")

    except FileNotFoundError:
        print("Error: Archivo no encontrado.\n")

    return ptokens

def actualizarToken(ptokens, pclave, pvalor):   
    """
    Funcionalidad:
        Actualiza un token existente si la clave ya está registrada,
        o agrega uno nuevo en caso contrario.

    Entradas:
        ptokens (list): Lista actual de tokens.
        pclave (str): Clave del token.
        pvalor (str): Valor asociado a la clave.

    Salidas:
        list: Lista de tokens actualizada.
    """
    
    for i, (c, v) in enumerate(ptokens):
        if c == pclave:
            print(f"Token '{pclave}' fue reescrito.")
            ptokens[i] = (pclave, pvalor)
            return ptokens

    ptokens.append((pclave, pvalor))
    return ptokens

def mostrarTokens(ptokens):   
    """
    Funcionalidad:
        Muestra en pantalla todos los tokens almacenados.

    Entradas:
        ptokens (list): Lista de tokens registrados.

    Salidas:
        None: Solo imprime información en pantalla.
    """
    if not ptokens:
        print("No hay tokens cargados.\n")
        return

    print("\n=== TOKENS CARGADOS ===")
    for clave, valor in ptokens:
         print(f"{clave}  →  {valor}")
         print()

def agregarModificarToken(ptokens):   
    """
    Funcionalidad:
        Permite agregar nuevos tokens o modificar tokens existentes 
        mediante entrada manual del usuario.

    Entradas:
        ptokens (list): Lista actual de tokens.

    Salidas:
        list: Lista de tokens actualizada.
    """
    print("\n=== AGREGAR / MODIFICAR TOKENS ===")
    print("Escriba 'cancelar' para salir.\n")

    cadenas = input("Ingrese la cadena con los tokens: ").strip()

    if cadenas.lower() == "cancelar":
        confirmacion = input("Esta seguro que quiere cancelar? Digite Y para confirmar, N para volver: ")
        if confirmacion == 'Y':
            print ("Operación cancelada.\n") 
        else:
            print (cadenas)
        return ptokens

    separador = input("Seleccione su separador ('->', '=' o ','): ").strip()

    if separador not in ["->", "=", ","]:
        print("Separador inválido.\n")
        return ptokens

   
    if separador == ",":
        listaTokens = cadenas.split(",")

        for token in listaTokens:
            token = token.strip()

            
            if "->" in token:
                partes = token.split("->")
            elif "=" in token:
                partes = token.split("=")
            else:
                print(f"Formato inválido en: {token}")
                continue

            if len(partes) == 2:
                clave = partes[0].strip()
                valor = partes[1].strip()

                existe = False
                for c, v in ptokens:
                    if c == clave:
                        existe = True
                        break

                if existe:
                    print(f"El token '{clave}' ya existe. Se actualizará.")
                else:
                    print(f"El token '{clave}' será añadido.")

                ptokens = actualizarToken(ptokens, clave, valor)

    else:
        partes = cadenas.split(separador)

        if len(partes) == 2:
            clave = partes[0].strip()
            valor = partes[1].strip()

            existe = False
            for c, v in ptokens:
                if c == clave:
                    existe = True
                    break

            if existe:
                print(f"El token '{clave}' ya existe. Se actualizará.")
            else:
                print(f"El token '{clave}' será añadido.")

            ptokens = actualizarToken(ptokens, clave, valor)
        else:
            print("Formato inválido.\n")

    print("Proceso terminado.\n")
    return ptokens

def guardarTokens(ptokens):    
    """
    Funcionalidad:
        Guarda los tokens actuales en un archivo de texto utilizando
        el separador indicado por el usuario.

    Entradas:
        ptokens (list): Lista de tokens a guardar.

    Salidas:
        None: Genera un archivo con los tokens.
    """

    if not ptokens:
        print ('No hay tokens para guardar. \n')
        return

    nombreArchivo = input ('Ingrese nombre del archivo a utilizar: ')
    separador = input ('Ingrese el tipo de separador que desea utilizar: ')
    if separador not in ["->", "=",  ","]:
        print ("Separador inválido. Seleccione '='', '->'' o ','")
        separador = input("Ingrese tipo de separador: ").strip()
    try:
        with open (nombreArchivo, "w") as archivo:
             for clave, valor in ptokens:
                linea = clave + separador + valor + "\n"
                archivo.write(linea)
        print ('Tokens guardados correctamente.\n')
    except:
        print("Ocurrió un error al guardar el archivo.\n")
               
def traducirCodigo (ptokens): 
    """
    Funcionalidad:
        Traduce un archivo de código reemplazando las palabras que coincidan
        con las claves de los tokens y genera un nuevo archivo traducido.
        Además, contabiliza la cantidad de reemplazos realizados.

    Entradas:
        ptokens (list): Lista de tokens (clave, valor).

    Salidas:
        dict: Diccionario con la cantidad de reemplazos por cada clave.
        None: Si el archivo no es encontrado.
    """
    conteo = {}

    for clave, _ in ptokens:
       conteo [clave] = 0
   
    archivoInicial = input('Digite el nombre del archivo a traducir: ')
    archivoSalida = input('Ingrese el nombre del nuevo archivo: ')
    try:
        with open(archivoInicial, 'r') as archivoLectura, \
             open(archivoSalida, 'w') as archivoEscritura:
                for linea in archivoLectura:

                    palabraActual = ""
                    nuevaLinea = ""

                    for caracter in linea:
                        if caracter.isalnum() or caracter == "_":
                            palabraActual += caracter
                        else:
                            if palabraActual != "":
                                traducida= palabraActual
                                for clave, valor in ptokens:
                                    if palabraActual == clave:
                                        traducida = valor
                                        conteo [clave]+= 1
                                        break

                                    nuevaLinea += traducida
                                    palabraActual = ""
                                    nuevaLinea += caracter

                    if palabraActual != "":
                        traducida = palabraActual
                        for clave, valor in ptokens:
                            if palabraActual == clave:
                                traducida = valor
                                conteo [clave] += 1
                                break

                        nuevaLinea += traducida
                        archivoEscritura.write(nuevaLinea)
                        print("Archivo traducido correctamente.\n")
        return conteo

    except FileNotFoundError:
        print("Archivo no encontrado.\n")
        return None 
   


def reporteCSV (ptokens, conteo): 
    """
    Funcionalidad:
        Genera un archivo CSV con el reporte de los tokens reemplazados
        y la cantidad de veces que fueron utilizados.

    Entradas:
        ptokens (list): Lista de tokens.
        conteo (dict): Diccionario con la cantidad de reemplazos.

    Salidas:
        None: Genera el archivo 'reporte.csv'.
    """
    if conteo is None:
        print ("No hay datos para generar el reporte indicado. \n")


    with open ('reporte.csv', "w") as archivo:
        archivo.write ('pralabra original, Token de reemplazo, Cantidad \n')

        for clave,valor in ptokens:
            cantidad = conteo.get (clave,0)

            if cantidad > 0:
                linea = f"{clave},{ptokens}, {valor}."
                archivo.write(linea)


def reporteHTML (ptokens):  
    """
    Funcionalidad:
        Genera un reporte en formato HTML con título personalizado
        y fecha/hora de generación.

    Entradas:
        ptokens (list): Lista de tokens (no se modifica).

    Salidas:
        None: Genera un archivo HTML con el reporte.
    """
    import datetime
    reporteTitulo = input ('Ingrese el titulo que desea imporner en el reporte: ')
    ahora=datetime.datetime.now()
    fechaConFormato = ahora.strftime("%d-%m-%y-%H-%M-%S")
    nombreArchivo= f"reporteHTML_{fechaConFormato}.html"
    with open (nombreArchivo, "w",encoding="utf-8") as archivo:
          archivo.write(f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{reporteTitulo}</title>
</head>
<body>
    <h1>{reporteTitulo}</h1>
    <p>Fecha y hora de generación: {ahora.strftime("%d/%m/%y %H:%M:%S")}</p>
</body>
</html>
""")
    
    print(f"Reporte generado correctamente: {nombreArchivo}")

import pickle 
import datetime
import os    
def bitacoraRegistros(ptokens):      
    """
    Funcionalidad:
        Carga la bitácora almacenada previamente si existe,
        o crea una nueva lista vacía si no hay registros.

    Entradas:
        ptokens (list): Lista de tokens (no se utiliza directamente).

    Salidas:
        list: Lista de registros almacenados en la bitácora.
    """

    if os.path.exists("bitacora.txt"):
        with open ("bitacora.txt", "rb") as archivo:
            return pickle.load(archivo)
    else:
        return []
def guardarBitacora(bitacora):
    with open ("bitacora.txt", "wb") as archivo:
        pickle.dump (bitacora,archivo)

def registrarEvento(bitacora,descripcion):  
    """
    Funcionalidad:
        Registra un nuevo evento en la bitácora con fecha y hora actual.

    Entradas:
        bitacora (list): Lista de eventos.
        descripcion (str): Descripción del evento.

    Salidas:
        None: Agrega el evento y guarda la bitácora.
    """
    ahora = datetime.datetime.now()
    fecha = ahora.strftime ("%Y-%m-%d_%H:%M:%S")
    registro = (fecha, descripcion)
    bitacora.append(registro)
    guardarBitacora(bitacora)

def buscarPalabra (bitacora, palabra):  
    """
    Funcionalidad:
        Busca en la bitácora eventos que contengan una palabra clave.

    Entradas:
        bitacora (list): Lista de registros.
        palabra (str): Palabra a buscar.

    Salidas:
        None: Imprime los registros coincidentes.
    """
     
    for registro in bitacora:
            if palabra.lower() in registro[1].lower():
                print(registro)

def buscarFecha(bitacora,fechaBuscar):   
    """
    Funcionalidad:
        Busca registros en la bitácora que coincidan con una fecha específica.

    Entradas:
        bitacora (list): Lista de registros.
        fechaBuscar (str): Fecha a consultar (formato YYYY-MM-DD).

    Salidas:
        None: Imprime los registros encontrados.
    """
    for registro in bitacora:
        if fechaBuscar in registro[0]:
            print(registro)
       
def submenu(bitacora): 
    """
    Funcionalidad:
        Muestra un submenú que permite consultar la bitácora por fecha
        o por palabra clave.

    Entradas:
        bitacora (list): Lista de registros.

    Salidas:
        None: Ejecuta acciones según la opción seleccionada.
    """
    while True:
        print ("\n *** Submenú Bitácora ***")
        print ('1 para acciones por día escogido \n 2 para ver las acciones con palabras claves \n 3 para salir del submenú')

        opciones = input ("Seleccione alguna opción: ")
        if opciones == "1":
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
            buscarFecha(bitacora, fecha)
        elif opciones == "2":
         buscarPalabra
        else:
            return
        
   


                              


                    
                
   
    
    



def menu ():  
    """
    Funcionalidad:
        Muestra el menú principal del sistema y permite ejecutar
        todas las funcionalidades disponibles del programa.

    Entradas:
        None.

    Salidas:
        None: Controla el flujo completo del sistema.
    """
    tokens = []
    bitacora = bitacoraRegistros(tokens)

    while True:
        print ('menu')
        print ('='*20)
        print ('\n 1: cargar archivo \n 2: Mostar tokens \n 3: Agregar/modificar token \n 4: Guardar tokens \n 5: Traducir código \n 6: Generar CSV \n 7: Generar HTML \n 8: Submenú de bitácora del sistema')
        opcion= input('Seleccione una acción: ')
        if opcion == "1":
            tokens = cargarArchivo(tokens)
            registrarEvento(bitacora, "Se cargaron tokens desde archivo")

        elif opcion == "2":
            mostrarTokens(tokens)
            registrarEvento(bitacora, "Se mostraron los tokens")

        elif opcion == "3":
            tokens = agregarModificarToken(tokens)
            registrarEvento(bitacora, "Se agregaron/modificaron tokens")

        elif opcion == "4":
            guardarTokens(tokens)
            registrarEvento(bitacora, "Se guardaron los tokens")

        elif opcion == "5":
            conteo = traducirCodigo(tokens)
            registrarEvento(bitacora, "Se tradujo un archivo")

        elif opcion == "6":
            conteo = traducirCodigo(tokens)
            reporteCSV(tokens, conteo)
            registrarEvento(bitacora, "Se generó reporte CSV")

        elif opcion == "7":
            reporteHTML(tokens)
            registrarEvento(bitacora, "Se generó reporte HTML")

        elif opcion == "8":
            submenu(bitacora)

        elif opcion == "9":
            registrarEvento(bitacora, "El usuario salió del programa")
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.\n")

print (menu ())    

