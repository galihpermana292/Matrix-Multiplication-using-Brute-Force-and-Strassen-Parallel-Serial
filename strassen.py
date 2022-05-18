import numpy as np
import time
import multiprocessing


def split(matrix):
    """
    Splits a given matrix into quarters.
    Input: nxn matrix
    Output: tuple containing 4 n/2 x n/2 matrices corresponding to a, b, c, d
    """
    row, col = matrix.shape
    row2, col2 = row//2, col//2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]
 
 
def proses(max1, res, pos):
  res.append({"mat": max1, "idx": pos})
  
def proses2(sum, res, pos):
  res.append({"sum": sum, "idx": pos})
 
def strassen(x, y):

    """
    Computes matrix product by divide and conquer approach, recursively.
    Input: nxn matrices x and y
    Output: nxn matrix, product of x and y
    """
 
    # Base case when size of matrices is 1x1
    if len(x) == 1:
        return x * y
 
    # Splitting the matrices into quadrants. This will be done recursively
    # until the base case is reached.
    a, b, c, d = split(x)
    e, f, g, h = split(y)
 
    # Computing the 7 products, recursively (p1, p2...p7)
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
    
    # p1 = np.matmul(a, f-h)
    # p2 = np.matmul(a+b, h)   
    # p3 = np.matmul(c+d, e)      
    # p4 = np.matmul(d, g-e)      
    # p5 = np.matmul(a+d, e+h)      
    # p6 = np.matmul(b-d, g+h)
    # p7 = np.matmul(a-c, e+f) 
    
    
    # p1 = strassen(a, f - h) 
    # p1 = a.dot(f-h)
    # p2 = strassen(a + b, h)
    # p2 = a+b.dot(h)   
    # p3 = strassen(c + d, e)
    # p3 = c+d.dot(e)
    # p4 = strassen(d, g - e)
    # p4 = d.dot(g-e)
    # p5 = strassen(a + d, e + h)
    # p5 = a+d.dot(e+h)
    # p6 = strassen(b - d, g + h)
    # p6 = b-d.dot(g+h)
    # p7 = strassen(a - c, e + f)
    # p7 = a-c.dot(e+f)
    
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
    # c11 = newList[4]['mat'] + newList[3]['mat'] - newList[1]['mat'] + newList[5]['mat']
    # c12 = newList[0]['mat'] + newList[1]['mat'] 
    # c21 = newList[2]['mat'] + newList[3]['mat']
    # c22 = newList[0]['mat'] + newList[4]['mat'] - newList[2]['mat'] - newList[6]['mat']
    
    # c11 = p5 + p4 - p2 + p6 
    # c12 = p1 + p2          
    # c21 = p3 + p4           
    # c22 = p1 + p5 - p3 - p7 
 
    # Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
    c = np.vstack((np.hstack((newList2[0]['sum'], newList2[1]['sum'])), np.hstack((newList2[2]['sum'], newList2[3]['sum']))))
    # c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
 
    # return server1.append(c)
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
    print(A)
    print(B)
    start = time.time()
    C = strassen(A, B)
    stop = time.time()
    exec_time = stop - start
    print("Hasil: ")
    print(C)
    print(f"execution time = {exec_time}")
