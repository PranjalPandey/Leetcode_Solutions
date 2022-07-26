class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        p = -1
        ans = ""
        while abs(p)<=max(len(a),len(b)):
            value = carry
            if abs(p)<=len(a):
                value+=int(a[p])
            
            if abs(p)<=len(b):
                value+=int(b[p])
                
            carry = value//2
            value%=2
            ans+=str(value)
            p-=1
        if carry:
            ans+= str(carry)
        return ans[::-1]
                