from time import sleep
import os
import numpy as np
import useful_functions as uf       # useful_functions.py 

# Useful for showing complete matrix
np.set_printoptions(threshold=np.nan)

# We can reduce the DIM to 20, because
# the greatest difference, which is in datos_modified.txt,
# is 9, so, we must have a minimal interval from -10 to 9 
DIM = 40
# size of window equals to 18, doesn't detect anomaly
WINDOWSIZE = 5

if os.path.exists("datos.txt"):
    with open("datos.txt") as f:
        try:
            increments = uf.get_differences([int(linea) for linea in f])
            # print(increments)
            # print(len(increments))
        except IOError:
            print("\nThe file datos.txt doesn't exist.\n")
            exit()

    # transition matrix (square matrix)
    TM = uf.get_transition_matrix(DIM, increments)

    uf.satisfy_condition(TM, DIM)
    print("Minimum value: ",TM.min())
    print("Maximum value: ",TM.max())

    THRESHOLD = uf.minimum_likelihood(increments, TM, WINDOWSIZE)
    print("Minimum likelihood: ",THRESHOLD)

    # datos_modificados has an anomaly in line 38752
    uf.detect_anomalies_from_file("datos_modificados.txt", TM, THRESHOLD, WINDOWSIZE)

    print("\nWe're starting with the serial port.....")
    uf.detect_anomalies_real_time('/dev/cu.usbmodem1421', 9600, TM, THRESHOLD, WINDOWSIZE)
