class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr_tank,total_tank,start=0,0,0
        
        for i in range(len(gas)):
            total_tank+=gas[i]-cost[i]
            curr_tank+=gas[i]-cost[i]
            if curr_tank<0:
                curr_tank=0
                start = i+1
        return start if total_tank>=0 else -1
            
        