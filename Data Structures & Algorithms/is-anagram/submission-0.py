class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        teen = {}
        for char in s:
            if char in seen:
                seen[char] += 1;
            else:
                seen[char] = 1;
        
        for char in t:
            if char in teen:
                teen[char] += 1;
            else:
                teen[char] = 1;
        
        return teen == seen