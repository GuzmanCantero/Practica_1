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
Ayer se cambiaron los nombres de todos los sensores, como "AmbientHumidity" a "humidity_rh", e incluso se añadió uno nuevo, pero el programa funciona con los nuevos nombres de sensores. No habrá problemas con ellos.  

Los datos mostrados se ven mucho mejor con cantidades de tiempo largas, como es de esperar en una gráfica.  

La humedad y temperatura eran los únicos datos que planeaba enseñar, pero al ser tan estables añadí un parámetro de concentración para mostrar la fluctuación de datos en la gráfica y evitar que se muestre únicamente una línea recta.  

El .py tiene capacidad de albergar todos los datos de todos los sensores si fuera necesario, y añadirlos es muy accesible, pero para la práctica sólo recoge los datos mencionados anteriormente.
