"""
39. 组合总和
中等
相关标签
相关企业
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。

对于给定的输入，保证和为 target 的不同组合数少于 150 个。



示例 1：

输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
示例 2：

输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
示例 3：

输入: candidates = [2], target = 1
输出: []


提示：

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
candidates 的所有元素 互不相同
1 <= target <= 40

"""

'''
1. 先排序，如果 sub_sum > target 即为终止条件
2. 递归回溯：遍历所有可能的组合，
3. 减枝：超出目标值，则终止路径遍历
'''

from utils import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start, sub_list, sub_sum):
            if sub_sum == target:
                res.append(sub_list.copy())
                return
            if sub_sum > target:
                return
            for i in range(start, len(candidates)):
                if candidates[i] + sub_sum > target:
                    break
                sub_list.append(candidates[i])
                backtrack(i, sub_list, sub_sum + candidates[i])
                sub_list.pop()


        backtrack(0, [], 0)

        return res


# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates.sort()  # 排序以便剪枝
#         res = []
#
#         def backtrack(start, sub_list, sub_sum):
#             if sub_sum == target:
#                 res.append(list(sub_list))  # 添加当前组合的副本
#                 return
#             if sub_sum > target:
#                 return  # 剪枝，当前路径不可能满足条件
#             for i in range(start, len(candidates)):
#                 num = candidates[i]
#                 if sub_sum + num > target:
#                     break  # 后续元素更大，无需继续
#                 sub_list.append(num)
#                 backtrack(i, sub_list, sub_sum + num)  # 允许重复使用当前元素
#                 sub_list.pop()  # 回溯
#
#         backtrack(0, [], 0)
#         return res

if __name__ == '__main__':
    solve_batch(
        Solution, [
            ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ]
    )
