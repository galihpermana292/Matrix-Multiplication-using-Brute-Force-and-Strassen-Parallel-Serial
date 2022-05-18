# Multiply two square matrices of order n by thedefinition based algorithm
# input: two n-by-n matrices A and B
# output: matrix C = AB

import random
import numpy as np
import time
import multiprocessing


def proses ( sum, res, idx, pos):
  if(idx == 0):
    res.insert(pos, sum)
  else:
    res[pos] = res[pos]+sum 
  

def matrix_multiplication(A, B):
    global xxx
    t_start = time.time()
    C = []
    for i in range(len(A)):
        col_C =[]
        for j in range(len(B[i])):
            for k in range(len(B)):
                p1 = multiprocessing.Process(target=proses, args=(A[i][k] * B[k][j], server1, k, j, ))
                p1.start()
                p1.join()
            col_C.append(server1[j])
        C.append(col_C)
    t_finish = time.time()
    print('execution time=', t_finish - t_start)
    return C

if __name__ == "__main__":
  with multiprocessing.Manager() as manager:
    server1 = manager.list([])
    print('insert n for n-by-n matrices A and B')
    n = int(input())
    rows, cols = (n, n)

# method 2
    # A = []
    # B = []
    # for i in range(rows):
    #     col_A = []
    #     col_B = []
    #     for j in range(cols):
    #         col_A.append(random.randint(0, 9))
    #         col_B.append(random.randint(0, 9))
    #     A.append(col_A)
    #     B.append(col_B)
    
    
    # A = np.array([[1, 3], [2, 3]])
    # B = np.array([[1, 4], [3, 3]])
    
    A = np.random.randint(5, size=(n, n))
    B = np.random.randint(5, size=(n, n))

    C = matrix_multiplication(A, B)
    # print(A)
    # print(B)
    # print(C)
    
