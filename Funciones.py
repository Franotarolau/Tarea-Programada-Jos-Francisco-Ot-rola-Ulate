
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

    return tokens

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
        confirmacion = input("Esta seguro que quiere cancelar? Digite Y para confirmar, N para volver")
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

          

   
    
    



def menu ():
    tokens = []

    while True:
        print ('='*20)
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
        else:
            print("Opción inválida.\n")

print (menu ())    

