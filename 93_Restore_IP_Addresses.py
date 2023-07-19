from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        start=0
        ip=[]
        n=len(s)
        def backtracking(numberDot:int,start:int):
            if numberDot==0:
                if start==n or (s[start]=='0' and len(s[start:])>1):
                    return
                elif int(s[start:])<=255:
                    ip.append(s[start:])
                    res.append('.'.join(ip))
                    ip.pop()
                    return
                else:
                    return
            for end in range(start+1,n):
                if int(s[start:end])<=255 and int(s[start:end])>0:
                    ip.append(s[start:end])
                    backtracking(numberDot-1,end)
                    ip.pop()
                elif int(s[start:end])==0:
                    ip.append(s[start:end])
                    backtracking(numberDot-1,end)
                    ip.pop()
                    break
        backtracking(3,0)
        return res
s ="255255255255"
so=Solution()
print(so.restoreIpAddresses(s))