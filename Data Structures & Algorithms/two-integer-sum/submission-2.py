class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {};
        for i in range(len(nums)):
            map[nums[i]] = i;
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in map and map[comp] != i:
                return [i, map[comp]];

        return [];