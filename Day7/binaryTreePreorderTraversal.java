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
    public List<Integer> preorderTraversal(TreeNode root) {
        
        List<Integer> theList = new ArrayList<Integer>();
        
        preOrder(root, theList);
        
        return theList;
        
    }
    
    public void preOrder(TreeNode root, List<Integer> theList) {
        
        if(root == null) {
            return;
        }
        
        theList.add(root.val);
        
        preOrder(root.left, theList);
        
        preOrder(root.right, theList);
        
    }
}