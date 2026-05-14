class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #i do not know what a defaultdict is 
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
        #also explain the list(res.values())