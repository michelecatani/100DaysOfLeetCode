class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        String prefix = strs[0];
        
        if(strs.length == 1) {
            return prefix;
        }
        
        for(int i = 1; i < strs.length; i++) {
            
            if(strs[i].length() < prefix.length()) {
                prefix = prefix.substring(0, strs[i].length());
            }
            
            int length = prefix.length();
            
            for(int j = 0; j < length; j++) {
                if(prefix.equals(strs[i].substring(0, prefix.length()))) {
                    break;
                } else {
                    if(prefix.length() == 1) {
                        return "";
                    }
                    prefix = prefix.substring(0, prefix.length() - 1);
                }
            }
        }
            
        return prefix;
        
    }
}
