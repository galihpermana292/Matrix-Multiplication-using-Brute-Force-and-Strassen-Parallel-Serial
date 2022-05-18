import random
import time
from strassen import split, strassen

def matrix_multiplication(A, B):
    t_start = time.time()
    C = []
    for i in range(len(A)):
        col_C =[]
        for j in range(len(B[i])):
            x = 0
            for k in range(len(B)):
                x += A[i][k] * B[k][j]
            col_C.append(x)
        C.append(col_C)
    t_finish = time.time()
    print('execution time=', t_finish - t_start)
    return C

if __name__ == "__main__":
    print('insert n for n-by-n matrices A and B')
    n = int(input())
    rows, cols = (n, n)

    A = []
    B = []
    for i in range(rows):
        col_A = []
        col_B = []
        for j in range(cols):
            col_A.append(random.randint(0, 9))
            col_B.append(random.randint(0, 9))
        A.append(col_A)
        B.append(col_B)

    C = matrix_multiplication(A, B)
