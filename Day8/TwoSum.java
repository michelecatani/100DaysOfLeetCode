class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer, Integer> theMap = new HashMap<Integer, Integer>();
        
        int[] theArray = {0, 0};
        
        for(int i = 0; i < nums.length; ++i) {
            
            int diff = target - nums[i];
            
            if(theMap.containsKey(diff)) {
                
                theArray[0] = i;
                theArray[1] = theMap.get(diff);
                
                return theArray;
                
            } else {
                theMap.put(nums[i], i);   
            }
        }
        
        return theArray;
        
    }
}