from time import sleep
import os
import numpy as np
import useful_functions as uf

# Para mostrar matriz numpy completa
np.set_printoptions(threshold=np.nan)

DIM = 500
WINDOWSIZE = 5
USB = '/dev/cu.usbmodem1421'

if os.path.exists("datos.txt"):
    with open("datos.txt") as f:
        try:
            # Con el comando [int(linea) for linea in f] estamos 
            # construyendo un vector con cada linea del fichero.
            # Pasandoselo a la funcion get_increments estamos obteniendo 
            # el vector diferencia. 
            increments = uf.get_increments([int(linea) for linea in f])
        except IOError:
            print("\nThe file datos.txt doesn't exist.\n")
            exit()

    # Matriz de transición
    TM = uf.get_transition_matrix(DIM, increments) 

    uf.satisfy_condition(TM, DIM)
    print("Minimum value: ",TM.min())
    print("Maximum value: ",TM.max())

    THRESHOLD = uf.minimum_likelihood(increments, TM, WINDOWSIZE)
    print("Minimum likelihood: ",THRESHOLD)

    # datos_modificados tienen una anomalía en la línea 38752
    uf.detect_anomalies_from_file("datos_modificados.txt", TM, THRESHOLD, WINDOWSIZE)

    print("\nWe're starting with the serial port.....")
    # Se queda en bucle infinito, leyendo valores del puerto serial
    uf.detect_anomalies_real_time(USB, 9600, TM, THRESHOLD, WINDOWSIZE)
