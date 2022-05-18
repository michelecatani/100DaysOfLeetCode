class Solution {
    public int maxArea(int[] height) {
        
        int max = 0;
        
        int lp = 0;
        
        int rp = height.length - 1;
        
        while(lp < rp) {
            
            int theHeight = Math.min(height[lp], height[rp]);
            
            int theLength = rp - lp;
            
            max = Math.max(max, theHeight * theLength);
            
            if(height[lp] > height[rp]) {
                rp--;
            } else {
                lp++;
            }
        }
        
        return max;
    }  
}