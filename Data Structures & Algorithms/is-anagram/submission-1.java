class Solution {
    public boolean isAnagram(String s, String t) {
        int[] freqs = new int[26];


        for (int i = 0; i < s.length(); i++) {
            freqs[s.charAt(i) - 'a']++;
        }

        for (int i = 0; i < t.length(); i++) {
            freqs[t.charAt(i) - 'a']--;
        }

        for (int i = 0; i < freqs.length; i++) {
            if (freqs[i] != 0) return false;
        }
        return true;
    }
}
