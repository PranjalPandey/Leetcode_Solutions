class Solution:
    def dfs(self,image,sr,sc,color,host_color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return

        delta = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        for dx, dy in delta:
            x = sr + dx
            y = sc + dy
            if x >= 0 and x < len(image) and y >= 0 and y < len(image[0]) and image[x][y]==host_color:
                image[x][y] = color
                self.dfs(image, x, y, color,host_color)
        image[sr][sc]= color
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        host_color = image[sr][sc]
        if host_color!=color:
            self.dfs(image,sr,sc,color, host_color)
        return image