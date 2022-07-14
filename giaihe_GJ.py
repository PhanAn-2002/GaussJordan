
import numpy as np
import pandas as pd

df = pd.read_excel('giaihe.xlsx', header = None)
matrix = df.to_numpy()
# print(matrix)

index_row = []  
index_column = []  
result = np.zeros((len(matrix[0]) - 1, len(matrix[0])))


def find_pivot_element():    
    global index_row, index_column
    index_temp = []
    pivot_element = 0
    for row in range(0, len(matrix)):
        if row in index_row:
            continue  # Bỏ qua vì hàng này đã có phần tử giải
        max_row = np.amax(abs(matrix[row, 0:(len(matrix[0]) - 1)]))  # Tìm phần tử lớn nhất trong hàng row
        if (1 in matrix[row, 0:(len(matrix[0]) - 1)]) or (-1 in matrix[row, 0:(len(matrix[0]) - 1)]):  # Nếu có 1 hoặc -1 trong hàng row => chọn làm phần tử giải
            pivot_element = 1
            row_pivot_element = row
            index_temp = np.where(abs(matrix[row, 0:(len(matrix[0]) - 1)]) == pivot_element)
            index_temp = index_temp[:1]
            index_temp = index_temp[0][0]
            break
        elif max_row > pivot_element:  # Lưu giá trị phần tử giải, tìm vị trí trên ma trận
            pivot_element = max_row
            row_pivot_element = row
            index_temp = np.where(abs(matrix[row, 0:(len(matrix[0]) - 1)]) == pivot_element)
            index_temp = index_temp[:1]
            index_temp = index_temp[0][0]
    if pivot_element != 0:  # Lưu vị trí hàng và cột của phần tử giải
        index_row.append(row_pivot_element)
        index_column.append(int(index_temp))
#         print("Phan tu giai: ", round(matrix[index_row[-1]][index_column[-1]], 10))
#         print("Vi tri: ", index_row[-1] + 1, index_column[-1] + 1)
#         print()


def Gauss_Jordan_method():
    global matrix
    find_pivot_element()
    zeros_array = np.zeros((len(matrix), len(matrix[0])))  # Tạo 1 ma trận không
    for row in range(0, len(matrix)):
        if row == index_row[-1]:
            continue
        m = - matrix[row][index_column[-1]] / matrix[index_row[-1]][index_column[-1]]  # Tìm m
        zeros_array[row] = matrix[index_row[-1]] * m
    matrix = matrix + zeros_array
    
    
def normalize_pivot_element():
    for i in range(len(index_row)):
        matrix[index_row[i]] = matrix[index_row[i]] / matrix[index_row[i]][index_column[i]]
#     print(matrix)


def rank():
    rank1 = 0  # Hạng của ma trận hệ số A
    rank2 = 0  # Hạng của ma trận mở rộng
    for row in range(0, len(matrix)):
        if np.amax(abs(matrix[row, 0:(len(matrix[0]) - 1)])) > 0:
            rank1 = rank1 + 1
        if np.amax(abs(matrix[row, 0:len(matrix[0])])) > 0:
            rank2 = rank2 + 1
    if rank1 < rank2:
        print("He PT vo nghiem!")
        f=open("GJ_output.txt","w")
        f.write("He PT vo nghiem!")
        f.close()
    elif rank1 < (len(matrix[0]) - 1):
        print("He PT co vo so nghiem!")
        display_solutions()
    else:
        print("He PT co nghiem duy nhat!")
        display_solutions()
        

def display_solutions():
        
    global result
    for column in range(len(matrix[0]) - 1):
        if column in index_column:
            vt = index_column.index(column)
            result[column][0] = matrix[index_row[vt]][len(matrix[0]) - 1]
            for i in range(len(matrix[0]) - 1):
                if i not in index_column:
                    result[column][i + 1] = -matrix[index_row[vt]][i]
        else:
            result[column][column + 1] = 1

    # In ma trận result ra màn hình
    print('Ma tran ket qua:')
    print(result)
    print('===========================')
    print('Nghiem cua he phuong trinh (lam tron den 2 chu so):')
    for i in range(0, len(result)):
        print('X%d = ' %(i+1), end = '\t')
        for k in range(0, len(result[0])):
            if k == 0:
                print('%0.2f ' %(result[i,k]),end = '+ ')
            else:
                print('%0.2f.X%d ' %(result[i,k],k),end = '')
                if (k == (len(result[0])-1)):
                    print()
                else: print('+ ', end ='')                  
    # Xuất kết quả ra file output.txt
    np.savetxt('GJ_output.txt', result, fmt='%.5f')  # %.5f: lấy 5 chữ số sau dấu phẩy ghi vào file


is_all_zero = np.all((matrix == 0)) #Kiểm tra xem liệu ma trận chỉ chứa số 0 hay không
if is_all_zero:
    print('Loi vi ma tran chi chua 0') 
else:
    for i in range(0, min(len(matrix), len(matrix[0]))):
        Gauss_Jordan_method()
#         print(matrix)
#         print('===========================')
#     print("- - - - - Chuẩn hóa hệ số - - - - -")
    normalize_pivot_element()
#     print("- - - - - Kết luận - - - - -")
    rank()

