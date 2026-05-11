class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let s = new Set(nums);

        if (s.size !== nums.length) return true

        return false;
        }
}
