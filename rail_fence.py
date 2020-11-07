from itertools import cycle
import numpy as np

# Зашшифровать текст
def encode_rail_fence_cipher(string, n):

    try:
        matrix =  [[] for j in range(n)]
        counter = 0
        rail_pattern = list(range(n)) + list(range(n))[-2:0:-1]
    
        for item in cycle(''.join([str(x) for x in rail_pattern])):
            if counter >= len(string):
                break

            counter += 1 
            matrix[int(item)].append(string[counter-1])


    
        str_matrix = []
    
        for lst in matrix:
            str_matrix.append(''.join(lst))
    

        return ''.join(str_matrix)

    except:
        return 'Что-то пошло не так :/'




# Дешифровать текст
def decode_rail_fence_cipher(string, n):
    try:
        string = str(string)
        matrix =  [[] for j in range(n)]
        counter = 0
        counter_2 = 0
        rail_pattern = cycle(list(range(n)) + list(range(n))[-2:0:-1])
    
        indexes = sorted(range(len(string)), key=lambda i: next(rail_pattern))
        result = [''] * len(string)
    
        for i, c in zip(indexes, string):
            result[i] = c
        

        return ''.join(result)

    except:
        return 'Что-то пошло не так :/'