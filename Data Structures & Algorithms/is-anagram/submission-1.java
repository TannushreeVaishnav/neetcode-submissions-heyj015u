class Solution {
    public boolean isAnagram(String s, String t) {
    int m=s.length();
        int n=t.length();
        if(m!=n){
            return false;
        }
        int [] cnt=new int [26];
        for(int i=0;i<m;i++){
            cnt[s.charAt(i)-'a']++;
        }
        for(int j=0;j<n;j++){
            cnt[t.charAt(j)-'a']--;
        }
        for(int i=0;i<cnt.length;i++){
            if(cnt[i]!=0){
                return false;
            }
            
        }
        return true;

    }
}
