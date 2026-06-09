class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> charset=new HashSet<>();
        int maxlen=0;
        int l=0;
        for(int right=0;right<s.length();right++){
            while(charset.contains(s.charAt(right))){
                charset.remove(s.charAt(l));
                l++;
            }
            charset.add(s.charAt(right));
            maxlen=Math.max(maxlen,right-l+1);
        }
        return maxlen;
        
    }
}
