import collections


class Solution:
    def groupAnagrams(self, strs):
        # 创建一个默认字典用于存储排序后的字符串作为键，字符串列表作为值
        hash_dict = collections.defaultdict(list)
        # 遍历输入的字符串列表
        for s in strs:
            # 将字符串排序后拼接成一个新的字符串作为键
            key = "".join(sorted(s))
            # 将排序后的字符串作为键，原始字符串作为值，添加到字典中
            hash_dict[key].append(s)

        # 返回字典中所有值的列表
        return list(hash_dict.values())


if __name__ == "__main__":
    # 示例 1:
    # 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

    # 示例 2:
    # 输入: strs = [""]
    # 输出: [[""]]

    # 示例 3:
    # 输入: strs = ["a"]
    # 输出: [["a"]]

    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strs))

    strs = [""]
    print(solution.groupAnagrams(strs))

    strs = ["a"]
    print(solution.groupAnagrams(strs))
