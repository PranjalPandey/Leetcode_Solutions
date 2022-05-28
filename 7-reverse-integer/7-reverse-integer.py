class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num=0
        flag=0
        if x<0:
            flag=1
            x=-1*x
        while x!=0:
            num=(num*10)+x%10
            x=x//10
        ans=-1*num if flag==1 else num
        return(0 if ans<-2**31 or ans>2**31 else ans) 
            
        