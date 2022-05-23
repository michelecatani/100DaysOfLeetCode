class Solution {
    public boolean isSubsequence(String s, String t) {
        
        if(s.length() == 0) {
            return true;
        }
        
        int sCounter = 0;
        
        for(int i = 0; i < t.length(); i++) {
            char currentSChar = s.charAt(sCounter);
            
            if(t.charAt(i) == currentSChar) {
                sCounter++;
            }
            if(sCounter == s.length()) {
                return true;
            }
        }
        
        return false;
    }
}