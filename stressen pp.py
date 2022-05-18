import numpy as np
import time
import multiprocessing

# fixed

def split(matrix):
    row, col = matrix.shape
    row2, col2 = row//2, col//2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]
 
 
def proses(max1, res, pos):
  res.append({"mat": max1, "idx": pos})
  
def proses2(sum, res, pos):
  res.append({"sum": sum, "idx": pos})
 
def strassen(x, y):
    if len(x) == 1:
        return x * y

    a, b, c, d = split(x)
    e, f, g, h = split(y)
 
    p1 = multiprocessing.Process(target=proses, args=(np.matmul(a, f-h), server1, 0,))
    p2 = multiprocessing.Process(target=proses, args=(np.matmul(a+b, h), server1, 1,))
    p3 = multiprocessing.Process(target=proses, args=(np.matmul(c+d, e), server1, 2,))
    p4 = multiprocessing.Process(target=proses, args=(np.matmul(d, g-e), server1, 3,))
    p5 = multiprocessing.Process(target=proses, args=(np.matmul(a+d, e+h), server1, 4,))
    p6 = multiprocessing.Process(target=proses, args=(np.matmul(b-d, g+h), server1, 5,))
    p7 = multiprocessing.Process(target=proses, args=(np.matmul(a-c, e+f) , server1, 6,))
    
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    
    newList = sorted(server1, key=lambda d: d['idx']) 

    # Computing the values of the 4 quadrants of the final matrix c
    c11 = multiprocessing.Process(target=proses2, args=((newList[4]['mat'] + newList[3]['mat'] - newList[1]['mat'] + newList[5]['mat']), server2, 0,))
    c12 = multiprocessing.Process(target=proses2, args=((newList[0]['mat'] + newList[1]['mat']), server2, 1,))
    c21 = multiprocessing.Process(target=proses2, args=((newList[2]['mat'] + newList[3]['mat']), server2, 2,))
    c22 = multiprocessing.Process(target=proses2, args=((newList[0]['mat'] + newList[4]['mat'] - newList[2]['mat'] - newList[6]['mat']), server2, 3,))
  
    c11.start()
    c12.start()
    c21.start()
    c22.start()
    c11.join()
    c12.join()
    c21.join()
    c22.join()
    
    
    newList2 = sorted(server2, key=lambda d: d['idx']) 

    c = np.vstack((np.hstack((newList2[0]['sum'], newList2[1]['sum'])), np.hstack((newList2[2]['sum'], newList2[3]['sum']))))
    return c

if __name__ == "__main__":
  with multiprocessing.Manager() as manager:
    server1 = manager.list([])
    server2 = manager.list([])
    print("masukkan nilai n")
    n = int(input())
    
    # A = np.array([[1, 3], [2, 3]])
    # B = np.array([[1, 4], [3, 3]])
    
    A = np.random.randint(5, size=(n, n))
    B = np.random.randint(5, size=(n, n))
    # print(A)
    # print(B)
    start = time.time()
    C = strassen(A, B)
    stop = time.time()
    exec_time = stop - start
    print(f"execution time = {exec_time}")
