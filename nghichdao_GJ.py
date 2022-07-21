#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd

df = pd.read_excel('nghichdao2.xlsx', header = None)
matrix = df.to_numpy()
# print(matrix)

n = len(matrix)
index_row = []  
index_column = []
matrixE = np.zeros([n,n])
for i in range(n):
    matrixE[i,i] = 1.0

def find_pivot_element():
    global index_row, index_column, w
    index_temp = []
    pivot_element = 0
    for row in range(0, len(matrix)):
        if row in index_row:  # Bỏ qua vì hàng này đã có phần tử giải
            continue
        max_row = np.amax(abs(matrix[row, 0:(len(matrix[0]))]))  # Tìm phần tử lớn nhất trong hàng row
        if (1 in matrix[row, 0:(len(matrix[0]))]) or (
                -1 in matrix[row, 0:(len(matrix[0]))]):  # Nếu có 1 hoặc -1 trong hàng row => chọn làm phần tử giải
            pivot_element = 1
            row_pivot_element = row
            index_temp = np.where(abs(matrix[row, 0:(len(matrix[0]))]) == pivot_element)
            index_temp = index_temp[:1]
            index_temp = index_temp[0][0]
            break
        elif max_row > pivot_element:  # Lưu giá trị phần tử giải, tìm vị trí trên ma trận
            pivot_element = max_row
            row_pivot_element = row
            index_temp = np.where(abs(matrix[row, 0:(len(matrix[0]))]) ==pivot_element)
            index_temp = index_temp[:1]
            index_temp = index_temp[0][0]
    if pivot_element != 0: # Lưu vị trí hàng và cột của phần tử giải
        w = 1
        index_row.append(row_pivot_element)
        index_column.append(int(index_temp))
    else:
        w = -1
        print("Ma trận không khả nghịch!!!!")
#         quit()

def Gauss_Jordan_method():
    global matrix,matrixE
    find_pivot_element()
    zeros_array = np.zeros([n,n])  # Tạo 1 ma trận không
    z = np.zeros([n,n])  # Tạo 1 ma trận không
    for row in range(0, len(matrix)):
        if row == index_row[-1]:
            continue
        m = - matrix[row][index_column[-1]] / matrix[index_row[-1]][index_column[-1]] #Tìm m
        zeros_array[row] = matrix[index_row[-1]] * m
        z[row] = matrixE[index_row[-1]] * m
    matrix = matrix + zeros_array
    matrixE = matrixE+z
        
def normalize_pivot_element():
    for i in range(len(index_row)):
        matrixE[index_row[i]] = matrixE[index_row[i]] / matrix[index_row[i]][index_column[i]]
        matrix[index_row[i]] = matrix[index_row[i]] / matrix[index_row[i]][index_column[i]]

def sosanh(a, b, n):
    check = 0
    for i in range(n):
        if a[i] > b[i]: return 1
        elif a[i] < b[i]: return -1
    return  check

print("Gauss-Jordan method to find the inversed matrix")
is_all_zero = np.all((matrix == 0)) #Kiểm tra xem liệu ma trận chỉ chứa số 0 hay không
if is_all_zero:
    print('Loi vi ma tran chi chua 0') 
else:
    for i in range(0, n):
        Gauss_Jordan_method()
    normalize_pivot_element()
    print()

    for i in range(n):
        for j in range(0, n-i-1):
            if sosanh(matrix[j],matrix[j+1],n) == -1:
                for k in range(n):
                    matrix[j,k], matrix[j+1, k] = matrix[j+1, k], matrix[j, k]
                    matrixE[j, k], matrixE[j + 1, k] = matrixE[j + 1, k], matrixE[j, k]
    if w == -1: print('-----------------------')
    else: 
        print("Ma trận nghịch đảo là:")
        print(matrixE)
        print('-----------------------')

