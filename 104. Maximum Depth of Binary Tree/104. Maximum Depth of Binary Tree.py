#解题思路
#用递归的方法，当前节点的最大深度就是左节点的最大深度和右节点的最大深度之中取大的加一。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == "__main__":
    None

    
    
 # 第二种方法 ： 多年未见大佬出品
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def work(root, cc):
            if not root: return cc
            return max(work(root.left, cc + 1), work(root.right, cc + 1))
        return work(root, 0)
    
    
#第三种方法   辰星大佬出品

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        depth = 1        
        dp_last = [root]
        while True:
            dp_cur = []
            for node in dp_last:
                if node:                    
                    if node.left:
                        dp_cur.append(node.left)
                    if node.right:
                        dp_cur.append(node.right)
            if dp_cur:   
                depth += 1
                dp_last = dp_cur
            else:
                break
        return depth

    # 第四种方法  辰星大佬出品
    
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        cnt = 0        
        dp = [[root]]
        while dp[cnt]:            
            dp.append([])
            cnt += 1
            for node in dp[cnt - 1]:
                if node:                    
                    if node.left:
                        dp[cnt].append(node.left)
                    if node.right:
                        dp[cnt].append(node.right)
        dp.pop()                   
        return cnt
    
