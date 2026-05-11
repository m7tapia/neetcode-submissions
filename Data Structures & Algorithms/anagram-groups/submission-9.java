class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();

        int[] freqs = new int[26];

        for (int i = 0; i < strs.length; i++) {

            Arrays.fill(freqs, 0);

            for (int j = 0; j < strs[i].length(); j++) {
                freqs[strs[i].charAt(j) - 'a']++;
            }

            StringBuilder sb = new StringBuilder();

            for (int freq: freqs) sb.append(freq + "#");

            String frequency = String.valueOf(sb);


            if (!map.containsKey(frequency)) {
                map.put(frequency, new ArrayList());
            }
            map.get(frequency).add(strs[i]);
        }

        return new ArrayList<>(map.values());
    }
}
