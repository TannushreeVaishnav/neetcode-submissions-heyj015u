class Solution {
    public boolean isPalindrome(String s) {
        s=s.toLowerCase().replaceAll("[^A-Za-z0-9]","");
        int st=0;
        int ed=s.length()-1;
        while(st<=ed){
            if(s.charAt(st)!=s.charAt(ed)){
                return false;
            }
            st++;
            ed--;
        }
        return true;
    }
}
