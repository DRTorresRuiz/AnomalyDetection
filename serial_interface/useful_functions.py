import os
import numpy as np

def get_differences( values ):
    length = len(values)
    
    differences = []
    i = 0
    while i < length-1:
        
        f = values[i]
        s = values[i+1]
        
        differences.append(s - f)
        
        i += 1

    return differences

def get_transition_matrix( dimension, data_array):
    middle = int(dimension/2)
    length = len(data_array)
    transition_matrix = np.zeros([dimension,dimension])

    if length > 1:
        i = 0
        while i < length-1:
            transition_matrix[data_array[i]+middle][data_array[i+1]+middle] += 1
            i += 1
    
    transition_matrix[ transition_matrix == 0] += 10e-6

    i = 0
    while i < dimension:
        transition_matrix[i] = transition_matrix[i]/transition_matrix[i].sum() 
        i += 1
    
    return transition_matrix # a square matrix

def satisfy_condition(transition_matrix, dimension):
    i = 0
    condition = True 
    while i < dimension and condition:
        if float(transition_matrix[i].sum()) < 0.999999999:
            condition = False
        
        i += 1

    if not condition:
        print("The transition matrix is malformed.")
    else:
        print("The transition matrix is formed correctly.")
    
    return

def minimum_likelihood( values, transition_matrix, window_size ):
    length = len(values)
    middle = int(transition_matrix.shape[1]/2)
    minimum = 1

    i = 0
    while i < length-(window_size+1):
        j = 0
        likeli = 1
        while j < window_size:
            likeli *= transition_matrix[values[i+(j-1)]+middle][values[i+(j-1)+1]+middle]
            j += 1
        
        if likeli < minimum:
            minimum = likeli

        i += 1 

    return minimum

def detect_anomalies_from_file( file, transition_matrix, threshold, window_size):
    if os.path.exists(file):
        with open(file) as f:
            try:
                middle = int(transition_matrix.shape[1]/2) # square matrix

                values = [int(linea) for linea in f]
                increments = get_differences(values)
                
                length = len(increments)
                
                if length > 1:
                    minimum = 1

                    i = 0
                    while i < length-(window_size+1):
                        j = 0
                        likeli = 1
                        while j < window_size:
                            likeli *= transition_matrix[increments[i+(j-1)]+middle][increments[i+(j-1)+1]+middle]
                            j += 1
                        
                        if likeli < threshold:
                            # i + 2 --> +2 because "i" stats in 0 and increments has length (len(values)-1),
                            # and we want to show the line of the file passed by argument.
                            print("We have found an anomaly in lines [",i+2,", ",i+(j-1)+2,"] with value ",likeli)
                        
                        i += 1 
            except IOError:
                print("\nThe file ",file,"doesn't exist.\n")
    return 