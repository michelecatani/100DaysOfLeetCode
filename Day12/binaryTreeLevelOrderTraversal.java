/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        
        List<List<Integer>> masterList = new ArrayList<List<Integer>>();
        
        if(root == null) {
            
            return masterList;
            
        }
        
        Queue<TreeNode> q = new LinkedList();
        
        q.offer(root);
        
        while(!q.isEmpty()) {
            
            int curSize = q.size();
            
            List<Integer> newLevel = new ArrayList<Integer>();
            
            for(int i = 0; i < curSize; i++) {
                
                TreeNode cur = q.poll();
                
                newLevel.add(cur.val);
                
                if(cur.left != null) {
                    q.offer(cur.left);        
                }
                if(cur.right != null) {
                    q.offer(cur.right);
                }
                
            }            
            masterList.add(newLevel);            
        }
        
        return masterList;
        
    }
}