class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        last_row = [1]
        current_row = [1]
        for i in range(rowIndex):
            current_row = [1]
            for j in range(1,len(last_row)):
                current_row.append(last_row[j-1]+last_row[j])
            current_row.append(1)
            last_row = current_row.copy()                       
        return current_row