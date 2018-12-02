#分析：

#可以采用DFS方式或BFS方式遍历树，并对比节点值
#采用DFS方式时，对比根节点左右子树，交换其中一棵树的左右子树，对比对应的节点值
#采用BFS方式时，从两侧遍历同一层节点，比对对应节点值
#代码：

#DFS方式
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.ret = True
        def dfsCmp(p,q):
            if self.ret:
                if p and q:
                    # print "p:%d,q:%d"%(p.val,q.val)
                    if p.val != q.val:
                        self.ret = False
                        return self.ret
                    else:
                        q.left,q.right = q.right,q.left
                        dfsCmp(p.left,q.left)
                        dfsCmp(p.right,q.right)
                elif p or q:
                    self.ret = False
 
        if root:
            if root.left and root.right:
                dfsCmp(root.left,root.right)
            elif root.left or root.right:
                return False
        return self.ret
