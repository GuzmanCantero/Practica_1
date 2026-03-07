import json
import re

# El siguiente código tiene capacidad para mostrar los parámetros de todos los sensores,
# pero sólo se emplearán la temperatura y humedad en las gráficas.
# La humedad y temperatura se muestran correctamente, pero son tan estables que añadí la concentración Pm1p0
# para demostrar que la gráfica actualizaba los datos correctamente

co_ppm = []
co2_ppm = []
ch4_ppm = []
nh3_ppm = []
tvoc_ppb = []

pm1_0 = []
pm2_5 = []
pm4_0 = []
pm10 = []
humid = []
temp = []
voc_index = []
nox_index = []

with open("mqtt_capture","r") as file:
    lineas = file.readlines()
    for linea in lineas:
        if "Payload" in linea:
            payload = linea.split("Payload:")[1].strip()
            if "pm1_0" in payload:
                lista_sensores = json.loads(payload)
                for i in lista_sensores:
                    pm1_0.append(lista_sensores["pm1_0"])
                    pm2_5.append(lista_sensores["pm2_5"])
                    pm4_0.append(lista_sensores["pm4_0"])
                    pm10.append(lista_sensores["pm10"])
                    humid.append(lista_sensores["humidity_rh"])
                    temp.append(lista_sensores["temperature_c"])
                    voc_index.append(lista_sensores["voc_index"])
                    nox_index.append(lista_sensores["nox_index"])

            if "co_ppm" in payload:
                lista_sensores = json.loads(payload)
                for i in lista_sensores:
                    co_ppm.append(lista_sensores["co_ppm"])
                    co2_ppm.append(lista_sensores["co2_ppm"])
                    ch4_ppm.append(lista_sensores["ch4_ppm"])
                    nh3_ppm.append(lista_sensores["nh3_ppm"])
                    tvoc_ppb.append(lista_sensores["tvoc_ppb"])

datos = {
    "temp": temp,
    "humid": humid,
    "pm1_0": pm1_0
}

with open("grafica.txt","w") as file:
    json.dump(datos, file)


import matplotlib.pyplot as plt
import numpy as np
plt.plot(temp)
plt.plot(humid)
plt.plot(pm1_0)
plt.savefig("grafica.png")
