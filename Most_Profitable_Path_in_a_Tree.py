class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node: return 0
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            price_new_path = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, price_new_path)
            return node.val + max(left_gain, right_gain)
        
        dfs(root)
        return self.max_sum