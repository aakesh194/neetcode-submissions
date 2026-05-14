class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = [[]]
        map = {}
        for i, string in enumerate(strs):
            key = "".join(sorted(string))
            if key not in map:
                map[key] = []

            map[key].append(string)

        return list(map.values())

        #bruh lwk did it with seeing the algorithm english of the first solution and kinda asking gpt to fix a lot of the errors