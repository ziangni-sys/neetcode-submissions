class Solution {

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();
        for(String str : strs){
            int l = str.length();

            if(l < 10){
                res.append("00").append(l).append(str);
            }else if(l < 100){
                res.append("0").append(l).append(str);
            }else{
                res.append(l).append(str);
            }
        }
        return res.toString();
    }

    public List<String> decode(String str) {
        char[] s1 = str.toCharArray();
        int end = s1.length;
        List<String> res = new ArrayList<>();
        if(s1.length == 0){
            return res;
        }
        int k = 0;
        while(true){
            int length = (s1[k] - '0') * 100 + (s1[k+1] - '0') * 10 + s1[k+2] - '0';
            StringBuilder sb = new StringBuilder();
            for(int i = k + 3; i < length + k + 3; i++){
                sb.append(s1[i]);    
            }
            k = k + length + 3;
            res.add(sb.toString());
            //System.out.println(k);
            if(k >= end - 1) break;
        }
        return res;
    }
}






















