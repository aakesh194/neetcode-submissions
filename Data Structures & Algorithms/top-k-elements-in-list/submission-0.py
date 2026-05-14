class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        list = []
        for j in range(0, k):
            for i in range(len(freq)):
                value = 0
                if freq[i] > value:
                    value = i;
            list.append(value)
            i = i+1
        
        return list
