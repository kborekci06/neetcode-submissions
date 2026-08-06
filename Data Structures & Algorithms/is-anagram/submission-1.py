class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sAnagramDict = defaultdict(int)
        tAnagramDict = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for c1 in s:
            sAnagramDict[c1] +=1
        for c2 in t:
            tAnagramDict[c2] +=1

        if (sAnagramDict == tAnagramDict):
            return True
        else:
            return False