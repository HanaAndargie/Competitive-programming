class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.two = [[0] * (col + 1) for i in range(row + 1)]

        for i in range(row):
            prefix = 0
            for j in range(col):
                prefix += matrix[i][j]
                self.two[i + 1][j + 1] = prefix + self.two[i][j + 1]
       
    
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        second = self.two[row2 + 1][col2 + 1] - self.two[row1][col2 + 1] - self.two[row2 + 1][col1] + self.two[row1][
            col1]
        return second
      
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
