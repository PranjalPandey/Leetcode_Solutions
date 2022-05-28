class Solution:
    def change_direction(self, curr_dir, command):
        d=["S","W","N","E"]
        c=d.index(curr_dir)
        if command==-1:
            if c==3:
                curr_dir="S"
            else:
                curr_dir=d[c+1]
            return curr_dir
        if command==-2:
            if c==0:
                curr_dir="E"
            else:
                curr_dir=d[c-1]
            return curr_dir
    def move_forward(self,curr_pos,curr_dir):
        if curr_dir=="E":
            curr_pos[0]+=1
        elif curr_dir=="W":
            curr_pos[0]-=1
        elif curr_dir=="N":
            curr_pos[1]+=1
        elif curr_dir=="S":
            curr_pos[1]-=1
        return curr_pos    
            
            
        
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        maxd = 0 
        left = {'N':'W', 'W':'S', 'S':'E', 'E':'N'}
        right = {'N':'E', 'E':'S', 'S':'W', 'W':'N'}
        step = {'N':[0,1], 'W':[-1, 0], 'E':[1,0], 'S':[0,-1]}
        
        obstacle = set()
        for o in obstacles:
          
            obstacle.add((o[0], o[1]))
        
        x, y = 0, 0
        curr_dir = 'N'
        for com in commands:
            if com == -2:
                curr_dir = left[curr_dir]
            elif com == -1:
                curr_dir = right[curr_dir]
            else: # com > 0, we should go forward 
                cnt = 0 
                d = step[curr_dir]
                while cnt < com and (x+d[0], y+d[1]) not in obstacle:
                    x += d[0]
                    y += d[1]
                    maxd = max(maxd, x**2+y**2)
                    cnt += 1
        return maxd
        