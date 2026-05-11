class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        if (strs.length == 0) {
            return new ArrayList();
        }

        Map<String, List> map = new HashMap<>();


        int[] count = new int[26];

        for (String str: strs) {
            Arrays.fill(count, 0);
            for (char c: str.toCharArray()) {
                count[c-'a']++;
            }
        
            StringBuilder sb = new StringBuilder();

            for (int num: count) {
                sb.append(num);
                sb.append('#'); //need a seperator to seperate counts and avoid edge cases
            }

            String key = sb.toString();

            if (!map.containsKey(key)) {
                map.put(key, new ArrayList());
            }
            map.get(key).add(str);
        }

        return new ArrayList(map.values());

    }
}
