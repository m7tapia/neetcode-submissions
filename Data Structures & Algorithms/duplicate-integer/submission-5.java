class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for (int num: nums) {
            set.add(num);
        }

        if (set.size() != nums.length) return true;
        return false;
    }

    //solution 2: you create the set add the numbers in there, and if the set is the same size
    //as the array that means there were no dupes. If the set is shorter, that means there was
    //dupes.
}