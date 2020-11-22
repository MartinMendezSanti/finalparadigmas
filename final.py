import datetime
import csv

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
            clientes_csv = csv.DictReader(f)
            contador = 0
            for row in clientes_csv:
                if busqueda in row['Nombre']:
                    contador += 1
                    print(row)
            if contador == 0:
                print("No se encontró ningún cliente con el nombre ingresado")

    except IOError:
        print("Hubo un error al intentar abrir el archivo")

def BuscarUsuariosPorEmpresa(emp_buscada, archivo):
    try:
        with open (archivo) as f:
            empresas_csv = csv.reader(f)
            encabezadores = next(empresas_csv, None)
            contador = 0
            clientes_empresa = []
            cliente = next(empresas_csv, None)
            while cliente:
                if  emp_buscada in cliente[5]:
                    contador += 1
                    clientes_empresa.append(cliente)
                cliente = next(empresas_csv, None)
            if contador > 0:
                print("---------------------------------------------")
                print(f"Empresa: {emp_buscada}\nTotal Usuarios: {contador}")
                print("---------------------------------------------")
                print(encabezadores)
                for cliente in clientes_empresa:
                    print(cliente)
            else:
                print("No se encontraron usuarios para la empresa buscada. Verifique que ingresó correctamente el nombre de la empresa.")
    except IOError:
        print("Hubo un error al intentar abrir el archivo")
    except IndexError:
        print("Hubo un problema con los datos del archivo. Verifique que no se hayan eliminado columnas del mismo.")

def BuscarSaldoPorEmpresa(emp_buscada, archivo_clientes, archivo_viajes):
    try:
        with open (archivo_clientes) as f_clientes, open (archivo_viajes) as f_viajes:
            clientes_csv = csv.reader(f_clientes)
            viajes_csv = csv.reader(f_viajes)
            next(clientes_csv, None)
            next(viajes_csv, None) #Estos next son para saltear los encabezadores

            cliente = next(clientes_csv, None)
            viaje = next(viajes_csv, None)
            saldo = 0
            while cliente:
                print(f"{cliente[2]} = {viaje[0]}")
                while viaje and viaje[0] == cliente[2]:
                    try:
                        monto = float(viaje[2])
                    except ValueError:
                        print("Se detectó en la columna de monto un valor no numérico")
                    print(f"monto: {monto}")
                    saldo += monto
                    viaje = next(viajes_csv, None)
                cliente = next(clientes_csv, None)
            # while viaje:
            #     while cliente and viaje[0] == cliente[2]:
            #         try:
            #             monto = float(viaje[2])
            #         except ValueError:
            #             print("Se detectó en la columna de monto un valor no numérico")
            #         print(f"monto: {monto}")
            #         saldo += monto
            #         cliente = next(clientes_csv, None)
            #     viaje = next(viajes_csv, None)
            print("---------------------------------------------")
            print(f"{emp_buscada} ${saldo}")
            print("---------------------------------------------")
    except IOError:
        print("Hubo un error al intentar abrir el archivo")
    except IndexError:
        print("Hubo un problema con los datos del archivo. Verifique que no se hayan eliminado columnas del mismo.")


archivos_clientes = ['clientes.csv']
archivos_viajes = ['viajes.csv']
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
        f_clientes = input("Ingrese el nombre del archivo de clientes con el que desea trabajar:\n")
        if f_clientes in archivos_clientes:
            BuscarCliente(cliente, f_clientes)
        else:
            print("No existe el archivo ingresado")
        print("")
    elif opcion == 2:
        mensaje = "Búsqueda de Usuarios por empresa"
        GuardarLogs(mensaje)
        empresa = input("Ingrese el nombre de la empresa que desea buscar:\n")
        f_clientes = input("Ingrese el nombre del archivo de clientes con el que desea trabajar:\n")
        if f_clientes in archivos_clientes:
            BuscarUsuariosPorEmpresa(empresa, f_clientes)
        else:
            print("No existe el archivo ingresado")
        print("")
    elif opcion == 3:
        mensaje = "Consulta de saldo por empresa"
        GuardarLogs(mensaje)
        empresa = input("Ingrese el nombre de la empresa que desea buscar:\n")
        f_clientes = input("Ingrese el nombre del archivo de clientes con el que desea trabajar:\n")
        f_viajes = input("Ingrese el nombre del archivo de viajes con el que desea trabajar:\n")
        if f_clientes in archivos_clientes and f_viajes in archivos_viajes:
            BuscarSaldoPorEmpresa(empresa, f_clientes, f_viajes)
        else:
            print("No existe alguno de los archivos ingresados")
        print("")
    elif opcion == 4:
        print("Hola")
        print("")
    elif opcion == 5:
        print("Adios")
        print("")
    else:
        print("Opción Inválida")
        print("")
