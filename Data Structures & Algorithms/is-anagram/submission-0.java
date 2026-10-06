class Solution {
    public boolean isAnagram(String s, String t) {
       HashMap<Character, Integer> map = new HashMap<>();
       for(char si : s.toCharArray()){
            map.put(si, map.getOrDefault(si,0) + 1);
       }
       for(char ti : t.toCharArray()){
            map.put(ti, map.getOrDefault(ti,0) - 1);
       }
       for(int v: map.values()){
            if(v != 0){
                return false;
            }
       }
       return true;
    }
}
