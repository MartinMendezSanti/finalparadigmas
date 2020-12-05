import csv

def BuscarSaldoPorEmpresa():
    # try:
    #     with open ('viajes.csv') as f:
    #         viajes_csv = csv.reader(f)
    #         next(viajes_csv, None)
    #         viaje = next(viajes_csv, None)
    #         viajes_personas = []
    #         while viaje:
    #             persona = []
    #             documento = viaje[0]
    #             saldo_persona = 0
    #             persona.append(viaje[0])
    #             while viaje and viaje[0] == documento:
    #                 try:
    #                     monto = float(viaje[2])
    #                 except ValueError:
    #                     print("Se detectó en la columna de monto un valor no numérico")
    #                 saldo_persona += monto
    #                 viaje = next(viajes_csv, None)
    #             persona.append(saldo_persona)
    #             viajes_personas.append(persona)
    # except IOError:
    #     print("Error al abrir el archivo")
    # try:
    #     with open ('clientes.csv') as fc:
    #         clientes_csv = csv.reader(fc)
    #         next(clientes_csv, None)
    #

    try:
        with open ('clientes.csv') as fc:
            clientes_csv = csv.reader(fc)
            next(clientes_csv, None)#Este next es para saltear los encabezadores
            cliente = next(clientes_csv, None)
            while cliente:
                saldo = 0
                empresa = cliente[5]
                while cliente and cliente[5] == empresa:
                    with open ('viajes.csv') as fv:
                        viajes_csv = csv.reader(fv)
                        viaje = next(viajes_csv, None)
                        while viaje:
                            if viaje[0] == cliente[2]:
                                try:
                                    monto = float(viaje[2])
                                except ValueError:
                                    print("Se detectó en la columna de monto un valor no numérico")
                                saldo += monto
                            viaje = next(viajes_csv, None)
                    cliente = next(clientes_csv, None)
                print("---------------------------------------------")
                print(f"{empresa}: ${saldo}")
    except IOError:
        print("Error al abrir el archivo de clientes")


BuscarSaldoPorEmpresa()
