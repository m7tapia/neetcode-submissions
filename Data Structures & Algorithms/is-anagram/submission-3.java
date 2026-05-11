class Solution {
    public boolean isAnagram(String s, String t) {
        int[] freq = new int[26];
        //each index corresponds to a letter in alphabet
        //0 -> a, 1 -> b...

        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
        }

        for (int i = 0; i < t.length(); i++) {
            freq[t.charAt(i) - 'a']--;
        }

        for (int i: freq) {
            if (i != 0) return false;
        }
        return true;
    }
}
