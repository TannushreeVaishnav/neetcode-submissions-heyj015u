class Solution {
    public int maxArea(int[] heights) {
        int l=0;
        int r=heights.length-1;
        int maxwater=0;
        while(l<r){
            int area=Math.min(heights[l],heights[r])*(r-l);
            maxwater=Math.max(maxwater,area);
            if (heights[l]<heights[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return maxwater;
    }
}
