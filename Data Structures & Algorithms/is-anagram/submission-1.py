class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_d = dict()
        t_d = dict()

        for i in s:
            s_d[i] = s_d.get(i,0) +1
        for j in t:
            t_d[j] = t_d.get(j,0) +1

        return s_d == t_d

