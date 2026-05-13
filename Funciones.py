
def cargarArchivo(ptokens):
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
    for i, (c, v) in enumerate(ptokens):
        if c == pclave:
            print(f"Token '{pclave}' fue reescrito.")
            ptokens[i] = (pclave, pvalor)
            return ptokens

    ptokens.append((pclave, pvalor))
    return ptokens

def mostrarTokens(ptokens):
    if not ptokens:
        print("No hay tokens cargados.\n")
        return

    print("\n=== TOKENS CARGADOS ===")
    for clave, valor in ptokens:
         print(f"{clave}  →  {valor}")
         print()

def agregarModificarToken(ptokens):
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
    import datetime
    reporteTitulo = input ('Ingrese el titulo que desea imporner en el reporte: ')
    ahora=datetime.datetime.now
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
    
    print(f"Reporte generado correctamente: {nombre_archivo}")

    

    
    



                              


                    
                
   
    
    



def menu ():
    tokens = []

    while True:
        print ('menu')
        print ('='*20)
        print ('\n 1: cargar archivo \n 2: Mostar tokens \n 3: Agregar/modificar token \n 4: Guardar tokens \n 5: Traducir código \n 6: Generar CSV \n 7: Generar HTML \n 8: Submenú de bitácora del sistema')
        opcion= int(input('Seleccione una acción: '))
        if opcion == 1:
            tokens = cargarArchivo(tokens)
            print ('se ha cargado el archivo correctamente.')\
            
        elif opcion == 2:
            mostrarTokens(tokens)

        elif opcion == 3:
            tokens = agregarModificarToken(tokens)
        elif opcion == 4:
            guardarTokens(ptokens)
        elif opcion == 5:
            traducirCodigo
        elif opcion==6:
            reporteCSV
        elif opcion == 7:
            reporteHTML

        else:
            print("Opción inválida.\n")

print (menu ())    

