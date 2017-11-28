from BinaryTreeRightSideView import TreeNode


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None
        node = TreeNode(t1.val if t1 else 0 + t2.val if t2 else 0)
        node.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        node.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return node


if __name__ == "__main__":
    solution = Solution()