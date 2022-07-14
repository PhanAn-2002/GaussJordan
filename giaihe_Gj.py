import numpy as np  

class Gauss_Jordan:
    np.set_printoptions(suppress=True, linewidth=np.inf, precision=10)  
    matrix = np.loadtxt("GJ_input.txt", delimiter=' ')  
    index_row = []  
    index_column = []  
    result = np.zeros((len(matrix[0]) - 1, len(matrix[0])))  
    
    def kt_ptg(self):
        """gói tìm phần tử giải"""
        index_temp = []
        pivot_element = 0
        for row in range(0, len(self.matrix)):
            if row in self.index_row:
                continue  
            max_row = np.amax(abs(self.matrix[row, 0:(len(self.matrix[0]) - 1)]))  
            if (1 in self.matrix[row, 0:(len(self.matrix[0]) - 1)]) or (
                    -1 in self.matrix[row,
                          0:(len(self.matrix[0]) - 1)]):  
                pivot_element = 1
                row_pivot_element = row
                index_temp = np.where(abs(self.matrix[row, 0:(len(self.matrix[0]) - 1)]) == pivot_element)
                index_temp = index_temp[:1]
                index_temp = index_temp[0][0]
                break
            elif max_row > pivot_element:  
                pivot_element = max_row
                row_pivot_element = row
                index_temp = np.where(abs(self.matrix[row, 0:(len(self.matrix[0]) - 1)]) == pivot_element)
                index_temp = index_temp[:1]
                index_temp = index_temp[0][0]
        if pivot_element != 0: 
            self.index_row.append(row_pivot_element)
            self.index_column.append(int(index_temp))            

    def tt_Gauss_Jordan(self):
        """Phương pháp Gauss - Jordan"""
        
        self.kt_ptg()
        zeros_array = np.zeros((len(self.matrix), len(self.matrix[0])))  
        for row in range(0, len(self.matrix)):
            if row == self.index_row[-1]:
                continue
            m = - self.matrix[row][self.index_column[-1]] / self.matrix[self.index_row[-1]][
                self.index_column[-1]] 
            zeros_array[row] = self.matrix[self.index_row[-1]] * m
        self.matrix = self.matrix + zeros_array

    def chuanhoa_ptg(self):
        """Gói chuẩn hóa hệ số """
        for i in range(len(self.index_row)):
            self.matrix[self.index_row[i]] = self.matrix[self.index_row[i]] / self.matrix[self.index_row[i]][
                self.index_column[i]]
        

    def rank(self):
        """Gói kiểm tra rank"""
        rank1 = 0  # Hạng của ma trận hệ số A
        rank2 = 0  # Hạng của ma trận mở rộng
        for row in range(0, len(self.matrix)):
            if np.amax(abs(self.matrix[row, 0:(len(self.matrix[0]) - 1)])) > 0:
                rank1 = rank1 + 1
            if np.amax(abs(self.matrix[row, 0:len(self.matrix[0])])) > 0:
                rank2 = rank2 + 1
        if rank1 < rank2:
            f=open("GJ_output.txt","w")
            f.write("He PT vo nghiem!")
            f.close()
        elif rank1 < (len(self.matrix[0]) - 1):
            f=open("GJ_output.txt","w")
            f.write("He PT co vo so nghiem!")
            f.close()
            self.Innghiem()
        else:
            f=open("GJ_output.txt","w")
            f.write("He PT co nghiem duy nhat!")
            f.close()
            self.Innghiem()
       

    def Innghiem(self):
        """Gói in ra nghiệm"""
        for column in range(len(self.matrix[0]) - 1):
            if column in self.index_column:
                vt = self.index_column.index(column)
                self.result[column][0] = self.matrix[self.index_row[vt]][len(self.matrix[0]) - 1]
                for i in range(len(self.matrix[0]) - 1):
                    if i not in self.index_column:
                        self.result[column][i + 1] = -self.matrix[self.index_row[vt]][i]
            else:
                self.result[column][column + 1] = 1
        
        # Xuất kết quả ra file output.txt
        np.savetxt('GJ_output.txt', self.result, fmt='%.5f')  
    
    def main(self):
        
        for i in range(0, min(len(self.matrix), len(self.matrix[0]))):
            self.tt_Gauss_Jordan()
            
        self.chuanhoa_ptg()
        
        self.rank()

try:
    RUN = Gauss_Jordan()
    RUN.main()
except:
    f = open("GJ_output.txt", "w")
    f.write("Da co loi xay ra!")
    f.close()

