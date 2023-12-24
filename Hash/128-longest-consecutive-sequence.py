class Solution:
    def longestConsecutive(self, nums):
        hash_dict = dict()
        res = 0
        for num in set(nums):
            if num not in hash_dict:
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)
                cur = left + right + 1
                res = max(res, cur)
                hash_dict[num - left] = cur
                hash_dict[num + right] = cur
        return res


if __name__ == "__main__":
    # 示例 1：
    # 输入：nums = [100,4,200,1,3,2]
    # 输出：4

    # 示例 2：
    # 输入：nums = [0,3,7,2,5,8,4,6,0,1]
    # 输出：9

    solution = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print(solution.longestConsecutive(nums))

    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(solution.longestConsecutive(nums))
