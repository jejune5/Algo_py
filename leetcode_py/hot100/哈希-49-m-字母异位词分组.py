"""
49. 字母异位词分组
中等
1.7K
相关企业
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的所有字母得到的一个新单词。



示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2:

输入: strs = [""]
输出: [[""]]
示例 3:

输入: strs = ["a"]
输出: [["a"]]


提示：

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母

"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}
        for item in strs:
            key = sorted(item).__str__()
            if key in hashtable:
                hashtable[key].append(item)
            else:
                hashtable[key] = [item]
        return [hashtable[key] for key in hashtable]


if __name__ == '__main__':
    sol = Solution()
    # [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    res = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(res)
