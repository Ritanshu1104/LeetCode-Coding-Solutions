class Solution:
    def processStr(self, s: str) -> str:
        res=""
        for i in s:
            if i.isalpha():
                res+=i
            elif i=="*":
                if res:
                    res=res[:len(res)-1]
            elif i=="#":
                res*=2
            else:
                res=res[::-1]
        return res
            