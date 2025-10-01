class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss=s.split(" ")
        if len(ss)!=len(pattern):
            return False
        map_ps={}
        map_sp={}
        for i in range(0,len(pattern)):
            c1=pattern[i]
            c2=ss[i]
            if (c1 in map_ps and map_ps[c1]!=c2) or (c2 in map_sp and map_sp[c2]!=c1):
                return False
            map_ps[c1]=c2
            map_sp[c2]=c1
        return True
