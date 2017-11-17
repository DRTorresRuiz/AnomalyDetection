from time import sleep
import os
import numpy as np
import useful_functions as uf       # useful_functions.py 

# Useful for showing complete matrix
np.set_printoptions(threshold=np.nan)

def main_function(dimension, values, window_size):
    increments = uf.get_differences(values)
    # print(increments)
    # print(len(increments))
    
    # transition matrix (square matrix)
    tm = uf.get_transition_matrix(dimension, increments) 

    uf.satisfy_condition(tm, dimension)
    print("Minimum value: ",tm.min())     
    print("Maximum value: ",tm.max())

    threshold = uf.minimum_likelihood(increments, tm, window_size)
    print("Minimum likelihood: ",threshold)
    
    # datos_modificados has an anomaly in line 38752
    uf.detect_anomalies_from_file("datos_modificados.txt", tm, threshold, window_size)

if os.path.exists("datos.txt"):
    with open("datos.txt") as f:
        try:
            # We can reduce the dimension to 20, because
            # the greatest difference, which is in datos_modified.txt,
            # is 9, so, we must have a minimal interval from -10 to 9 
            dimension = 40 
            window_size = 5 # size of window equals to 18, doesn't detect anomaly
            temperature = [int(linea) for linea in f]
            
            main_function(dimension,temperature,window_size)
            
        except IOError as e:
            print("\nThe file datos.txt doesn't exist.\n")