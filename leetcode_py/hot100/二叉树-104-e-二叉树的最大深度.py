"""

104. 二叉树的最大深度
简单
1.7K
相关企业
给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。



示例 1：





输入：root = [3,9,20,null,null,15,7]
输出：3
示例 2：

输入：root = [1,null,2]
输出：2


提示：

树中节点的数量在 [0, 104] 区间内。
-100 <= Node.val <= 100
"""

from typing import *
from utils.data_structure.TreeNode import *


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            l_height = self.maxDepth(root.left)
            r_height = self.maxDepth(root.right)
            return max(l_height, r_height) + 1
