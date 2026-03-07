#!/bin/bash

echo "Introduzca el tiempo de la captura en segundos:"
read tiempo

# si ya existe un mqtt_capture con datos, lo elimina para poder crear uno desde cero

if [ -f mqtt_capture ]; then
	rm -r mqtt_capture
fi

# el binario bloquea el resto de el programa, haciendo que nunca pueda esperar y matar el proceso
# al correrlo en segundo plano, no interrumpe el proceso

stdbuf -oL -eL ./Ejecutables/mqtt_subscribe_emqx_linux >> mqtt_capture 2>&1 &
PID=$!
sleep $tiempo

# marca el PID para matarlo posteriormente
echo $PID

# kill -0 no era suficiente
kill -9 $PID

python3 -m venv .venv
source .venv/bin/activate
sudo apt-get install jq

PYTHON_SCRIPT="sensores.py"
if [ -f "$PYTHON_SCRIPT" ]; then
	echo "Ejecutando $PYTHON_SCRIPT..."
	python3 "$PYTHON_SCRIPT"
else
	echo "Error: no se encontró $PYTHON_SCRIPT"
fi

jq -r '.temp[]' grafica.txt | gnuplot -e "
set terminal dumb size 100,30;
set title 'Temperatura';
plot '-' with lines
"
jq -r '.humid[]' grafica.txt | gnuplot -e "
set terminal dumb size 100,30;
set title 'Humedad';
plot '-' with lines
"
jq -r '.pm1_0[]' grafica.txt | gnuplot -e  "
set terminal dumb size 100,30;
set title 'PM1_0';
plot '-' with lines
"
