class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = set()
        
        def generate_subsets(nums, buffer, i):
            if i>=len(nums):
                output.add(tuple(sorted(buffer)))
                return
            generate_subsets(nums, buffer + [nums[i]], i+1)
            generate_subsets(nums, buffer , i+1)
                    
        generate_subsets(nums,[],0)
        return list(output)
        
                        
        