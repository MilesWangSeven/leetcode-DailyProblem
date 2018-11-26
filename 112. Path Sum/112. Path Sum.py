#解题思路
#直接通过递归来解决，判断一个节点时，先把要求的值先减去该节点的值，如果剩下要求的值为0且当前的节点就是一个叶子节点，
#那么从根节点到当前节点的路径就符合题目的要求。否则就要继续递归当前节点的左右节点。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        sum -= root.val
        if sum == 0 and root.left is None and root.right is None:
            return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


if __name__ == "__main__":
    None
