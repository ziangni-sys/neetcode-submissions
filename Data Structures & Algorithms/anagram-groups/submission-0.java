class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        HashMap<String, Integer> anapattern = new HashMap<>();
        for(int i = 0; i < strs.length; i++){
            char[] charas = strs[i].toCharArray();
            Arrays.sort(charas);
            String stri = new String(charas);
            if(anapattern.keySet().contains(stri)){
                int index = anapattern.get(stri);
                res.get(index).add(strs[i]);
            }else{
                anapattern.put(stri,res.size());
                List<String> subList = new ArrayList<>();
                subList.add(strs[i]);
                res.add(subList);
            }
        }
        System.out.print(anapattern);
        return res;
    }
}
