class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anapattern = new HashMap<>();
        for(int i = 0; i < strs.length; i++){
            char[] charas = strs[i].toCharArray();
            int[] count = new int[26];
            for(char c : charas){
                count[c - 'a']++;
            }
            StringBuilder sb = new StringBuilder();
            for(int c: count){
                sb.append(c).append("#");
            }
            String stri = sb.toString();
            anapattern.putIfAbsent(stri, new ArrayList<>());
            anapattern.get(stri).add(strs[i]);
        }
        //System.out.print(anapattern);
        return new ArrayList<>(anapattern.values());
    }
}
