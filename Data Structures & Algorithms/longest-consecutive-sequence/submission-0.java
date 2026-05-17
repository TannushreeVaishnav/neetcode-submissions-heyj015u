class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set=new HashSet<>();
        for(int i:nums){
            set.add(i);
        }
        int ans=0;
        for(int i : set){
            if (!set.contains(i-1)){
                int cur=i+1;
                while(set.contains(cur)){
                    cur+=1;
                }
                int lastel=cur-1;
                ans=Math.max(ans,lastel-i+1);
            }
        }
        return ans;
        
    }
}
