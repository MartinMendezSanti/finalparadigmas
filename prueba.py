import csv

lista_viajes = []
with open ('viajes.csv') as f_viajes:
    viajes_csv = csv.reader(f_viajes)
    next(viajes_csv, None) #Este next es para saltear los encabezadores
    viaje = next(viajes_csv, None)
    while viaje:
        lista_viajes.append(viaje)
        viaje = next(viajes_csv, None)

with open ('clientes.csv') as f_clientes:
    clientes_csv = csv.reader(f_clientes)
    next(clientes_csv, None) #Este next es para saltear los encabezadores
    cliente = next(clientes_csv, None)
    while cliente:
        empresa = cliente[5]
        while cliente and cliente[5] == empresa:
            for viaje in lista_viajes:
                if viaje[0] == cliente[2]:
                    print(f"{empresa}: {viaje[2]}")
            cliente = next(clientes_csv, None)
