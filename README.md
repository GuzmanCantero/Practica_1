# Practica_1
Práctica 1 de Sistemas Operativos

El siguiente .sh consiste en un código que ejecuta un ejecutable que detecta datos enviados mediante sensores, los guarda en un archivo, corre un .py que lee dicho archivo y lo procesa en un .txt en formato JSON, los imprime en una gráfica .png y muestra los datos como gráficas en ASCII en la terminal.

# Instalaciones necesarias:
-sudo apt install python3.12-venv
-sudo apt-get install jq
-sudo apt-get install gnuplot

# Archivos necesarios:
-Practica_1.sh
-sensores.py

# Archivos producidos:
-grafica.txt
-grafica.png

# Datos a recalcar
Desde las 12:00 hasta las 12:45 del 6/3, los sensores no muestran datos y no puedo demostrar que el programa funciona, a pesar de haberlo comprobado ayer. Probaré más adelante. (./Ejecutables/mqtt_subscribe_emqx_linux no muestra los datos, no es que los datos no aparezcan en el .txt)
<img width="968" height="187" alt="image" src="https://github.com/user-attachments/assets/3adfd848-a630-4563-88ed-7d0133e5b8d4" />
Los datos mostrados se ven mucho mejor con cantidades de tiempo largas, como es de esperar en una gráfica.
La humedad y temperatura eran los únicos datos que planeaba enseñar, pero al ser tan estables añadí un parámetro de concentración para mostrar la fluctuación de datos en la gráfica y evitar que se muestre únicamente una línea recta.
El .py tiene capacidad de albergar todos los datos de todos los sensores si fuera necesario, y añadirlos es muy accesible, pero para la práctica sólo recoge los datos mencionados anteriormente.
