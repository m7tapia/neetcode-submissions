class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length == 0) return new ArrayList();

        Map<String, List<String>> keys = new HashMap<>();

        int[] freqs = new int[26];

        for (String str: strs) {
            Arrays.fill(freqs, 0); //have to reset freq array after every string

            for (char ch: str.toCharArray()) {
                freqs[ch - 'a']++; //each character gets an index; 'a' - 'a' == 0; 'b' - 'a' == 1...     
            }

            StringBuilder sb = new StringBuilder();

            for (int count: freqs) {
                sb.append(count);
                sb.append('#');    //need this to avoid edge cases where different counts could blur together (like 10 then 1 could be mistaken for 1 then 0 then 10 without seperators
            }

            String key = String.valueOf(sb);

            if (!keys.containsKey(key)) {
                keys.put(key, new ArrayList());   //need to create the empty list for this key if it hasn't been created
            }
            keys.get(key).add(str); //add the string to the list of the corresponding key
        }

        return new ArrayList(keys.values());
    }
}
