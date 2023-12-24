class Solution:
    def twoSum(self, nums, target):
        # 创建一个字典用于存储数字和它们的索引
        hash_dict = dict()
        for i, num in enumerate(nums):
            # 如果字典中已经存在当前数字，则返回该数字的索引和之前出现的数字的索引
            if num in hash_dict:
                return [i, hash_dict.get(num)]
            # 否则将目标值减去当前数字的结果作为键，当前数字的索引作为值存入字典
            else:
                hash_dict[target - num] = i
        return []


if __name__ == "__main__":
    # 示例 1：
    # 输入：nums = [2,7,11,15], target = 9
    # 输出：[0,1]

    # 示例 2：
    # 输入：nums = [3,2,4], target = 6
    # 输出：[1,2]

    # 示例 3：
    # 输入：nums = [3,3], target = 6
    # 输出：[0,1]

    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums, target))

    nums = [3, 2, 4]
    target = 6
    print(solution.twoSum(nums, target))

    nums = [3, 3]
    target = 6
    print(solution.twoSum(nums, target))
