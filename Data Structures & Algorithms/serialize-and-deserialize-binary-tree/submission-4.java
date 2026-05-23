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

public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder result = new StringBuilder();
        if(root == null){
            return "";
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while(!queue.isEmpty()){
            TreeNode node = queue.poll();
            if(node != null){
                result.append(node.val+".");
                queue.offer(node.left);
                queue.offer(node.right);
            }else{
                result.append("#.");
            }
        }
        return result.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        System.out.println(data);
        Queue<TreeNode> queue = new LinkedList<>();
        int current = 0;
        if (data == null || data.isBlank()) {
            return null;
        }
        String[] tokens = data.split("\\.");
        TreeNode root = new TreeNode(Integer.parseInt(tokens[current++]));
        queue.offer(root);
        while(!queue.isEmpty()){
            System.out.println("Entering while loop");
            TreeNode node = queue.poll();
            String val =  tokens[current++];
            System.out.println("Value = "+val);
            if(!val.equals("#")){
                System.out.println("Now parsing int for :"+val);
                node.left = new TreeNode(Integer.parseInt(val));
                queue.offer(node.left);
            }
            val = tokens[current++];
            if(!val.equals("#")){
                node.right = new TreeNode(Integer.parseInt(val));
                queue.offer(node.right);
            }
        }
        return root;
    }
}
