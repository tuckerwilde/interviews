class Solution:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in xrange(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


    def permutetwo(self, nums):
        """
                :type nums: List[int]
                :rtype: List[List[int]]
                """

        def swap(i, j, nums):
            new_nums = list(nums)
            new_nums[i], new_nums[j] = new_nums[j], new_nums[i]
            return new_nums

        result = [nums, ]

        for i in range(len(nums) - 1):
            for one in result[:]:
                for j in range(i + 1, len(nums)):
                    result.append(swap(i, j, one))

        return result


Solution().permute([1,2,3])
Solution().permutetwo([1,2,3])