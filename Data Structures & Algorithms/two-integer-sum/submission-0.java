class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> w = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(w.keySet().contains(nums[i])){
                return new int[]{w.get(nums[i]),i};
            }else{
                w.put(target - nums[i], i);
            }
        }
        return new int[]{0,0};
    }
}
