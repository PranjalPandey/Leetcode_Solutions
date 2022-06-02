class Solution:
    def generate(self,output,buff,nums,i):
        if i >= len(nums):
            output.add(tuple(buff.copy()))
            return
        self.generate(output, buff+[nums[i]], nums, i+1)
        self.generate(output, buff, nums, i + 1)
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = set()
        buff = []
        self.generate(output, buff, nums, 0)
        return sorted([list(i) for i in output])
        