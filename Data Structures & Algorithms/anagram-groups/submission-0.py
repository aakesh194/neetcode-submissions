class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = [[]]
        for i, string in enumerate(strs):
            char = {}

            for j in range(len(string)):
                char[string[j]] = 1 + char.get(string[j], 0)

        #this is what i initially thought but maybe i can try using the one-pass counter from the anagram example

                

