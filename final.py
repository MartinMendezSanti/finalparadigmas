import datetime
import csv
import os


#En ambas funciones de verificación se decidió indicar por defecto la cantidad de elementos que debe tener la lista,
#en lugar de utilizar un len para calcularlo. Esto se pensó así para que se puedan detectar correctamente errores en los campos.
def VerificacionClientes(linea):
    #Esta función notifica cuando hay algún error en alguno de los campos pero no invalida el registro en caso de haberlo.
    #Si se invalidara traería problemas en los cálculos de saldos.
    for i in range (6):
        if len(linea[1]) == 0:
            print(f"Se detectó un campo sin datos para el cliente {linea[0]} DNI {linea[2]}")
    try:
        documento = int(linea[2])
    except ValueError:
        print(f"Se detectó un dato no numérico en el campo DNI del cliente {linea[0]}")

    if len(linea[2]) < 7 or len(linea[2]) > 8:
        print(f"El DNI debe contener entre 7 y 8 caracteres numéricos. Revise el documento para el cliente {linea[0]}")

    if "@" not in linea[4] or "." not in linea[4]:
        print(f"Se detectó un correo inválido para el cliente {linea[0]}")

def VerificacionViajes(linea):
    #Esta función notifica cuando hay algún error en alguno de los campos pero solo invalida el registro en caso de
    #que el error se encuentre en la columna de "monto". De esta manera se evitan los errores en el cálculo de los montos.
    flag = 0
    for i in range (3):
        if linea[i] == "":
            print(f"Se detectó un campo sin datos para el cliente {linea[0]} DNI {linea[2]}")

    try:
        documento = int(linea[0])
    except ValueError:
        print(f"Se detectó un dato no numérico en el campo DNI del cliente con documento {linea[0]}")

    if len(linea[0]) < 7 or len(linea[0]) > 8:
        print(f"El DNI debe contener entre 7 y 8 caracteres numéricos. Revise el documento para el cliente con documento {linea[0]}")

    try:
        nuevo_valor = linea[2].split(".")
        cantidad_decimales = len(nuevo_valor[1])
        if cantidad_decimales != 2:
            print(f"El monto detectado para el viaje del cliente DNI {linea[0]} del día {linea[1]} posee un error de formato")
            flag = 1
        monto = float(linea[2])
    except IndexError:
        print(f"El monto detectado para el viaje del cliente DNI {linea[0]} del día {linea[1]} posee un error de formato")
        flag = 1
    except ValueError:
        print(f"El monto detectado para el viaje del cliente DNI {linea[0]} del día {linea[1]} no es un valor numérico")
        flag = 1

    if flag == 0:
        return linea
    else:
        print(f"El registro para el viaje del cliente DNI {linea[0]} del día {linea[1]} no fue tenida en cuenta")
        return False



def IngresarOpcion():
    while True:
        opcion = input()
        try:
            return int(opcion)
        except ValueError:
            print("La opción ingresada no es válida. Recuerde que debe ingresar el NÚMERO de opción")

def GuardarLogs(accion):
    try:
        with open ("logs.txt", "a") as f:
            hora = str(datetime.datetime.now())
            f.write(f"{hora} : {mensaje}\n")

    except IOError:
        print("Hubo un error al intentar guardar los logs de la aplicación")

def BuscarCliente(busqueda, archivo):
    try:
        with open (archivo) as f:
            fieldnames = ['Nombre', 'Dirección', 'Documento', 'Fecha Alta', 'Correo Electrónico', 'Empresa']
            clientes_csv = csv.DictReader(f, fieldnames = fieldnames)
            contador = 0
            for row in clientes_csv:
                if busqueda in row['Nombre']:
                    contador += 1
                    print(row)
                    for campo in fieldnames:
                        if len(row[campo]) == 0:
                            print(f"El campo {campo} se encuentra vacío")
                    try:
                        documento = int(row['Documento'])
                    except ValueError:
                        print(f"El Documento del Cliente no corresponde a un valor numérico")
                    if len(row['Documento']) < 7 or len(row['Documento']) > 8:
                        print(f"El Documento del cliente es inválido")
                    if "@" not in row['Correo Electrónico'] or "." not in row['Correo Electrónico']:
                        print(f"El correo electrónico del cliente es inválido")
            if contador == 0:
                print("No se encontró ningún cliente con el nombre ingresado")

    except IOError:
        print("Hubo un error al intentar abrir el archivo")

def BuscarUsuariosPorEmpresa(archivo):

    #Si se desea que en lugar de mostrar los clientes de todas las empresas mueste solo los de una empresa que indique el cliente se puede
    #utilizar el siguiente código (pasando el nombre de la empresa como el parámetro emp_buscada)

    # try:
    #     with open (archivo) as f:
    #         empresas_csv = csv.reader(f)
    #         encabezadores = next(empresas_csv, None)
    #         contador = 0
    #         clientes_empresa = []
    #         cliente = next(empresas_csv, None)
    #         while cliente:
    #             if  emp_buscada in cliente[5]:
    #                 contador += 1
    #                 clientes_empresa.append(cliente)
    #             cliente = next(empresas_csv, None)
    #         if contador > 0:
    #             print("---------------------------------------------")
    #             print(f"Empresa: {emp_buscada}\nTotal Usuarios: {contador}")
    #             print("---------------------------------------------")
    #             print(encabezadores)
    #             for cliente in clientes_empresa:
    #                 print(cliente)
    #                 VerificacionClientes(cliente)
    #         else:
    #             print("No se encontraron usuarios para la empresa buscada. Verifique que ingresó correctamente el nombre de la empresa.")
    # except IOError:
    #     print("Hubo un error al intentar abrir el archivo")
    # except IndexError:
    #     print("Hubo un problema con los datos del archivo. Verifique que no se hayan eliminado columnas del mismo.")

    try:
        with open (archivo) as f:
            empresas_csv = csv.reader(f)
            encabezadores = next(empresas_csv, None)
            cliente = next(empresas_csv, None)
            clientes_empresa = []
            while cliente:
                empresa = cliente[5]
                clientes_empresa = []
                contador = 0
                while cliente and empresa == cliente[5]:
                    contador += 1
                    clientes_empresa.append(cliente)
                    cliente = next(empresas_csv, None)
                print("---------------------------------------------")
                print(f"Empresa: {empresa}\nTotal Usuarios: {contador}")
                print("---------------------------------------------")
                print(encabezadores)
                for usuario in clientes_empresa:
                    print(usuario)
                    VerificacionClientes(usuario)
    except IOError:
        print("Hubo un error al intentar abrir el archivo")
    except IndexError:
        print("Hubo un problema con los datos del archivo. Verifique que no se hayan eliminado columnas del mismo.")

def BuscarSaldoPorEmpresa(emp_buscada, archivo_clientes, archivo_viajes):


    try:
        #Se pasa el archivo viajes a una lista para así evitar tener que direccionar al Disco Rígido cada vez
        #que se necesitan leer datos del archivo. De esta forma el programa se hace mucho más eficiente.
        lista_viajes = []
        with open (archivo_viajes) as f_viajes:
            viajes_csv = csv.reader(f_viajes)
            next(viajes_csv, None) #Este next es para saltear los encabezadores
            viaje = next(viajes_csv, None)
            while viaje:
                lista_viajes.append(viaje)
                viaje = next(viajes_csv, None)
    except IOError:
        print("Hubo un error al intentar abrir el archivo de viajes")


    try:
        with open (archivo_clientes) as f_clientes:
            clientes_csv = csv.reader(f_clientes)
            next(clientes_csv, None) #Este next es para saltear los encabezadores
            cliente = next(clientes_csv, None)
            contador = 0
            while cliente:
                saldo = 0
                if emp_buscada in cliente[5]:
                    nueva_emp_buscada = cliente[5]
                    contador = 1
                    while cliente and cliente[5] == nueva_emp_buscada:
                        for viaje in lista_viajes:
                            if viaje[0] == cliente[2]:
                                flag = VerificacionViajes(viaje)
                                if flag is not False:
                                    try:
                                        monto = float(viaje[2])
                                    except ValueError:
                                        print("Se detectó en la columna de monto un valor no numérico en el archivo de viajes:")
                                    saldo += monto
                        cliente = next(clientes_csv, None)

                    print("---------------------------------------------")
                    print ("{0}: ${1:.2f}".format(nueva_emp_buscada, saldo))
                    print("---------------------------------------------")
                else:
                    cliente = next(clientes_csv, None)

            if contador == 0:
                print("No se encontró ningúna empresa que coincida con la búsqueda")

    except IOError:
        print("Hubo un error al intentar abrir el archivo")
    except IndexError:
        print("Hubo un problema con los datos del archivo. Verifique que no se hayan eliminado columnas del mismo.")

    # try:
    #     #Como el archivo de clientes no se ordena por el documento (que es el elemento que relaciona ambos archivos)
    #     # se debe ir iterando la lista de viajes por cada línea del archivo clientes que se procesa.
    #     with open (archivo_clientes) as f_clientes:
    #         clientes_csv = csv.reader(f_clientes)
    #         next(clientes_csv, None) #Este next es para saltear los encabezadores
    #         cliente = next(clientes_csv, None)
    #         while cliente:
    #             VerificacionClientes(cliente)
    #             saldo = 0
    #             empresa = cliente[5]
    #             while cliente and cliente[5] == empresa:
    #                 for viaje in lista_viajes:
    #                     if viaje[0] == cliente[2]:
    #                         flag = VerificacionViajes(viaje)
    #                         if flag is not False:
    #                             try:
    #                                 monto = float(viaje[2])
    #                             except ValueError:
    #                                 print("Se detectó en la columna de monto un valor no numérico en el archivo de viajes:")
    #                                 print(f"Cliente Documento {viaje[0]}, fecha de viaje {viaje[1]}")
    #                             saldo += monto
    #                 cliente = next(clientes_csv, None)
    #
    #             print("---------------------------------------------")
    #             print ("{0}: ${1:.2f}".format(empresa, saldo))
    #             print("---------------------------------------------")
    # except IOError:
    #     print("Hubo un error al intentar abrir el archivo")
    # except IndexError:
    #     print("Hubo un problema con los datos del archivo. Verifique que no se hayan eliminado columnas del mismo.")

    #Si no se quisiera pasar el archivo de viajes a lista y trabajarlo directamente desde el csv sería así:
        # try:
        #     with open ('clientes.csv') as fc:
        #         clientes_csv = csv.reader(fc)
        #         next(clientes_csv, None)#Este next es para saltear los encabezadores
        #         cliente = next(clientes_csv, None)
        #         while cliente:
        #             saldo = 0
        #             empresa = cliente[5]
        #             while cliente and cliente[5] == empresa:
        #                 with open ('viajes.csv') as fv:
        #                     viajes_csv = csv.reader(fv)
        #                     viaje = next(viajes_csv, None)
        #                     while viaje:
        #                         if viaje[0] == cliente[2]:
        #                             try:
        #                                 monto = float(viaje[2])
        #                             except ValueError:
        #                                 print("Se detectó en la columna de monto un valor no numérico")
        #                             saldo += monto
        #                         viaje = next(viajes_csv, None)
        #                 cliente = next(clientes_csv, None)
        #             print("---------------------------------------------")
        #             print(f"{empresa}: ${saldo}")
        # except IOError:
        #     print("Error al abrir el archivo de clientes")

def BuscarDatosTotalCliente(persona, archivo_clientes, archivo_viajes):

    try:
        #Se pasa el archivo viajes a una lista para así evitar tener que direccionar al Disco Rígido cada vez
        #que se necesitan leer datos del archivo. De esta forma el programa se hace mucho más eficiente.
        lista_viajes = []
        with open (archivo_viajes) as f_viajes:
            viajes_csv = csv.reader(f_viajes)
            encab_viajes = next(viajes_csv, None) #Este next es para saltear los encabezadores
            viaje = next(viajes_csv, None)
            while viaje:
                lista_viajes.append(viaje)
                viaje = next(viajes_csv, None)
    except IOError:
        print("Hubo un error al intentar abrir el archivo de viajes")

    try:
        with open (archivo_clientes) as f_clientes:
            clientes_csv = csv.reader(f_clientes)
            encabezadores = next(clientes_csv, None) #Este next es para guardar los encabezadores
            cliente = next(clientes_csv, None)
            contador = 0
            while cliente:
                if cliente[2] == persona:
                    contador += 1
                    print("---------------------------------------------")
                    print(f"Documento: {cliente[2]}")
                    print("---------------------------------------------")
                    VerificacionClientes(cliente)
                    print(encabezadores)
                    print(cliente)
                    saldo = 0
                    total_viajes = 0
                    datos_viajero = []
                    for viaje in lista_viajes:
                        if viaje[0] == cliente[2]:
                            flag = VerificacionViajes(viaje)
                            if flag is not False:
                                total_viajes += 1
                                datos_viajero.append(viaje)
                                try:
                                    monto = float(flag[2])
                                except ValueError:
                                    print("Se detectó en la columna de monto un valor no numérico en el archivo de viajes:")
                                    print(f"Cliente Documento {viaje[0]}, fecha de viaje {viaje[1]}")
                                saldo += monto
                    print("---------------------------------------------")
                    print("Total de viajes: {0}, Monto: ${1:.2f}".format(total_viajes, saldo))
                    print("---------------------------------------------")
                    if total_viajes > 0:
                        print(encab_viajes)
                        for elemento in datos_viajero:
                            print(elemento)
                cliente = next(clientes_csv, None)
            if contador == 0:
                print("\nNo se encontró ningún cliente con el documento ingresado")
    except IOError:
        print("Hubo un error al intentar abrir el archivo de clientes")

#archivos_clientes = ['clientes.csv']
#archivos_viajes = ['viajes.csv']
print("Bienvenido al gestor de facturación de PAR-Taxis")
mensaje = "Se inicia el programa"
GuardarLogs(mensaje)

opcion = 0
while opcion != 5:
    mensaje = "Menú"
    GuardarLogs(mensaje)
    print("Ingrese el número de opción que desea realizar")
    print("1 - Buscar cliente")
    print("2 - Ver usuarios por empresa")
    print("3 - Consultar el saldo en viajes por empresa")
    print("4 - Buscar el total de viajes y monto de un cliente")
    print("5 - Salir")
    opcion = IngresarOpcion()
    if opcion == 1:
        mensaje = "Búsqueda de Cliente por Nombre"
        GuardarLogs(mensaje)
        cliente = input("Ingrese el nombre del cliente que desea buscar:\n")
        f_clientes = input("Ingrese el nombre del archivo de clientes con el que desea trabajar (incluya el '.csv'):\n")
        #if f_clientes in archivos_clientes:
        if os.path.isfile(f_clientes) == True:
            BuscarCliente(cliente, f_clientes)
        else:
            print("No existe el archivo ingresado")
        print("")
    elif opcion == 2:
        mensaje = "Búsqueda de Usuarios por empresa"
        GuardarLogs(mensaje)
        f_clientes = input("Ingrese el nombre del archivo de clientes con el que desea trabajar (incluya el '.csv'):\n")
        #if f_clientes in archivos_clientes:
        if os.path.isfile(f_clientes) == True:
            BuscarUsuariosPorEmpresa(f_clientes)
        else:
            print("No existe el archivo ingresado")
        print("")
    elif opcion == 3:
        mensaje = "Consulta de saldo por empresa"
        GuardarLogs(mensaje)
        f_clientes = input("Ingrese el nombre del archivo de clientes con el que desea trabajar (incluya el '.csv'):\n")
        f_viajes = input("Ingrese el nombre del archivo de viajes con el que desea trabajar (incluya el '.csv'):\n")
        empresa = input("Ingrese el nombre de la empresa que desea buscar:\n")
        #if f_clientes in archivos_clientes and f_viajes in archivos_viajes:
        if os.path.isfile(f_clientes) == True and os.path.isfile(f_viajes) == True:
            BuscarSaldoPorEmpresa(empresa, f_clientes, f_viajes)
        else:
            print("No existe alguno de los archivos ingresados")
        print("")
    elif opcion == 4:
        mensaje = "Consultar total de viajes y monto por cliente"
        GuardarLogs(mensaje)
        cliente = input("Ingrese el Documento del cliente que desea buscar (sin puntos):\n")
        f_clientes = input("Ingrese el nombre del archivo de clientes con el que desea trabajar (incluya el '.csv'):\n")
        f_viajes = input("Ingrese el nombre del archivo de viajes con el que desea trabajar (incluya el '.csv'):\n")
        #if f_clientes in archivos_clientes and f_viajes in archivos_viajes:
        if os.path.isfile(f_clientes) == True and os.path.isfile(f_viajes) == True:
            BuscarDatosTotalCliente(cliente, f_clientes, f_viajes)
        else:
            print("No existe alguno de los archivos ingresados")
        print("")
    elif opcion == 5:
        mensaje = "Se sale del programa"
        GuardarLogs(mensaje)
        print("Adios")
        print("")
    else:
        print("Opción Inválida")
        print("")
