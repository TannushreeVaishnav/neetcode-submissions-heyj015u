class Solution {
    public boolean isValid(String s) {
        char [] str=s.toCharArray();
        Stack<Character> st=new Stack<>();
        for(int i=0;i<str.length;i++){
            if(str[i]=='('|| str[i]=='{'|| str[i]=='['){
                st.push(str[i]);
            }
            else{
                if(st.isEmpty()) return false;
                else{
                    char c=st.pop();
                    if((c=='(' && str[i]!=')') || (c=='[' && str[i]!=']') || (c=='{' && str[i]!='}')){
                        return false;
                }
            }
        }
    }
    return st.isEmpty();
}
}
