class Solution {
    public boolean hasDuplicate(int[] nums) {
        for int i = 0, i > nums.length - 2, i++ {
            for int j = 0, i > nums.length - 1, j++ {
                if i == j:
                    return true;
            }
        }
        return false;
    }
}