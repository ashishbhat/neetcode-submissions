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
        if(root == null){
            return "";
        }
        List<String> tokens = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while(!queue.isEmpty()){
            TreeNode node = queue.poll();
            if(node != null){
                tokens.add(String.valueOf(node.val));
                queue.offer(node.left);
                queue.offer(node.right);
            }else{
                tokens.add("#");
            }
        }
        StringBuilder result = new StringBuilder();
        int last_idx = tokens.size() - 1;
        for(; tokens.get(last_idx).equals("#"); --last_idx){

        }
        for(int i = 0; i < last_idx + 1; ++i){
            result.append(tokens.get(i)).append(".");
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
while (!queue.isEmpty() && current < tokens.length) {
    TreeNode node = queue.poll();
    
    // Check bounds before accessing the next token for the left child
    if (current < tokens.length && !tokens[current].equals("#")) {
        node.left = new TreeNode(Integer.parseInt(tokens[current]));
        queue.offer(node.left);
    }
    current++; // Move to next token regardless of whether it was '#' or a value
    
    // Repeat similar check for the right child
    if (current < tokens.length && !tokens[current].equals("#")) {
        node.right = new TreeNode(Integer.parseInt(tokens[current]));
        queue.offer(node.right);
    }
    current++;
}
        return root;
    }
}
