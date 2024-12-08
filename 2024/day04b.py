import numpy as np
from collections import defaultdict as dd

conv_map = dd(lambda: 0)
conv_map['M'] = 1
conv_map['A'] = 2
conv_map['S'] = 3

with open('word_search.txt', 'r') as file:
    input_matrix = np.array(list(map(lambda x: [conv_map[a] for a in x], list(map(lambda x: x.strip(), file.readlines())))))

m, n = len(input_matrix), len(input_matrix[0])

key = np.array([[1, 0, 1],
                [0, 2, 0],
                [3, 0, 3]])
search_matrix = np.array([[1, 0, 1],
                          [0, 1, 0],
                          [1, 0, 1]])

times_appear = 0

for i in range(m - 2):
    for j in range(n - 2):
        matrix = input_matrix[i:i+3, j:j+3] * search_matrix
        for _ in range(4):
            if (matrix == key).all():
                times_appear += 1
                break
            key = np.rot90(key)

print(times_appear)
