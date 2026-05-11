class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();

        for (int num: nums) {
            if (set.contains(num)) return true;
            set.add(num);
        }
        return false;

        //solution 1: you're checking before you add it in the set and if it's already in the set
        //you return true
    }
}