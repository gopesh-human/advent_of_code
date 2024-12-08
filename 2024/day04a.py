import numpy as np

with open('word_search.txt', 'r') as file:
    input_matrix = np.array(list(map(list, list(map(lambda x: x.strip(), file.readlines())))))

m, n = len(input_matrix), len(input_matrix[0])

def check_word(s):
    if s == 'XMAS' or s == 'SAMX':
        return True
    return False

times_appear = 0

for i in range(m):
    for j in range(n - 3):
        row = input_matrix[i:i+1, j:j+4][0]
        word = ''.join(row)
        if check_word(word):
            times_appear += 1

for i in range(m - 3):
    for j in range(n - 3):
        diag = []
        for k in range(4):
            diag.append(input_matrix[i+k, j+k])
        word = ''.join(diag)
        if check_word(word):
            times_appear += 1
for i in range(m - 3):
    for j in range(n - 3):
        diag = []
        for k in range(4):
            diag.append(input_matrix[i+k, (3+j)-k])
        word = ''.join(diag)
        if check_word(word):
            times_appear += 1

input_matrix = input_matrix.transpose()
for i in range(m - 3):
    for j in range(n):
        col = input_matrix[j:j+1, i:i+4][0]
        word = ''.join(col)
        if check_word(word):
            times_appear += 1
            
print(times_appear)
