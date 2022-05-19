class Solution {
    public boolean checkIfExist(int[] arr) {
        
        HashSet<Integer> theSet = new HashSet<Integer>();
        
        for(int cur: arr) {
            
            if(theSet.contains(cur)) return true;
            
            theSet.add(cur * 2);
            
            if(cur % 2 == 0) theSet.add(cur / 2);
            
        }
        
        return false;
        
    }
}