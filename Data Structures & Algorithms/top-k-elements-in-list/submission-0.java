class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>(); 
        for(int num : nums){
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        int[] res = new int[k];
        for(int i = 0; i < k; i++){
            int freq = -1;
            int max = nums[0];
            for(int num : map.keySet()){
                if(map.get(num) > freq){
                    max = num;
                    freq = map.get(num);
                }
            }
            res[i] = max;
            map.remove(max);
        }
        return res;
    }
}
