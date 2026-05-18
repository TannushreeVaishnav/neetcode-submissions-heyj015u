class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer,Integer> mp=new HashMap<>();
        mp.put(0,1);
        int res=0;
        int pref=0;
        for(int num:nums){
            pref+=num;
            if (mp.containsKey(pref-k)){
                res+=mp.get(pref-k);
            }
            mp.put(pref,mp.getOrDefault(pref,0)+1);
        }
        return res;
    }
}