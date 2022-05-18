class Solution {
    
    public boolean searchRow(int[] row, int target) {
        
        int low = 0;
        int high = row.length - 1;
        
        while(low <= high) {
            
            int mid = low + ((high - low) / 2);
            
            if(row[mid] == target) return true;
            else if (row[mid] > target) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        
        return false;
    }
    
    public boolean searchMatrix(int[][] matrix, int target) {
        
        int low = 0;
        int high = matrix.length - 1;
        
        while (low <= high) {
            
            int mid = low + ((high - low) / 2);
            
            if(matrix[mid][0] > target) {
                high = mid - 1;
            } else if (matrix[mid][matrix[mid].length - 1] >= target) {
                return searchRow(matrix[mid], target);
            } else {
                low = mid + 1;
            }
        }
        
        return false;
    }
    
}