class Solution {
    public int majorityElement(int[] nums) {
        int cnt=0;
        int elem=0;
        int n=nums.length;
        for(int i=0;i<n;i++){
            if(cnt==0){
                cnt=1;
                elem=nums[i];
            }
            else if(nums[i]==elem){
                cnt++;
            }
            else{
                cnt--;
            }
        }
        return elem;
    }
}