class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix = filter(lambda a: a[0]<=target and target<=a[len(a)-1],matrix)
        # print(list(matrix))
        for row in (matrix):
            if target in row:
                return True
        return False
        