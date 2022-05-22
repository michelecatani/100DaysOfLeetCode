class Solution {
    public String reverseWords(String s) {
        String after = s.trim().replaceAll(" +", " ");
        
        String[] newS = after.split(" ");
        
        StringBuilder sb = new StringBuilder();
        
        for(int i = newS.length - 1; i >= 0; i--) {
            sb.append(newS[i]);
            sb.append(" ");
        }
        
        return sb.toString().trim();
    }
}