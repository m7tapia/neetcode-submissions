class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length == 0) return new ArrayList();

        HashMap<String, List> map = new HashMap<>();

         int[] freq = new int[26];

        for (int i = 0; i < strs.length; i++) {
            Arrays.fill(freq, 0);

            for (int j = 0; j < strs[i].length(); j++) {
                freq[strs[i].charAt(j) - 'a']++;
            }

            StringBuilder sb = new StringBuilder();

            for (int num: freq) {
                sb.append(num + "$");
            }

            String key = String.valueOf(sb);

            if (!map.containsKey(key)) {
                map.put(key, new ArrayList());
            }
            map.get(key).add(strs[i]);
        
        }

        return new ArrayList(map.values());
    }
}
