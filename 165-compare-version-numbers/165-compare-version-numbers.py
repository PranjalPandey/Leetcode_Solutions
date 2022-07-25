class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split('.')
        v2=version2.split('.')
        if len(v1)>len(v2):
            while len(v2)!=len(v1):
                v2.append('0')
        elif len(v1)<len(v2):
            while len(v2)!=len(v1):
                v1.append('0')
        i=0
        while i<len(v1):
            if int(v1[i])>int(v2[i]):
                flag=1
                break
            elif int(v1[i])<int(v2[i]):
                flag=-1
                break
            else:
                flag=0
            i+=1
        return flag