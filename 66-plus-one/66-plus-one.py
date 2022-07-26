class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer = len(digits)-1
        carry = 0 
        digits[-1]+=1
        while pointer >= 0:
            value = carry
            value+=digits[pointer]
            carry = value//10
            value = value%10
            digits[pointer] = value
            pointer-=1
        if carry:
            return [carry]+digits
        return digits
        
        