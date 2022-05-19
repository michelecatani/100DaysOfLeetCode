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
    public List<Integer> inorderTraversal(TreeNode root) {
        
        List<Integer> theList = new ArrayList<Integer>();
        
        inorder(root, theList);
        
        return theList;
    }
    
    public void inorder(TreeNode root, List<Integer> theList) {
        
        if(root == null) {
            return;
        }
        
        inorder(root.left, theList); // first we visit left child
        
        theList.add(root.val); // then we visit root
        
        inorder(root.right, theList); // then we visit right child 
        
    }
}