class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out =[]
        rowStart = 0
        rowEnd = len(matrix)-1
        colStart = 0
        colEnd = len(matrix[0])-1
        
        while rowStart<=rowEnd and colStart<=colEnd:
            
            for e in range(colStart,colEnd+1):
                out.append(matrix[rowStart][e])
            rowStart+=1
            for e in range(rowStart,rowEnd+1):
                out.append(matrix[e][colEnd])
            colEnd-=1
            if rowStart<=rowEnd:
                for e in range(colEnd,colStart-1,-1):
                    out.append(matrix[rowEnd][e])
                rowEnd-=1
            if colStart<=colEnd:
                for e in range(rowEnd,rowStart-1,-1):
                    out.append(matrix[e][colStart])
                colStart+=1
        return out
            
        