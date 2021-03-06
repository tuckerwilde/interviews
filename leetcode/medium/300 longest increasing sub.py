class Solution(object):
#using dP
    def lengthOfLIS1(self, nums):
        if not nums:
            return 0
        dp = [1]*len(nums)
        for i in range (1, len(nums)):
            for j in range(i):
                if nums[i] >nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

    #using binary search
    def lengthOfLIS(self, nums):
        def search(temp, left, right, target):
            if left == right:
                return left
            mid = left+(right-left)/2
            return search(temp, mid+1, right, target) if temp[mid]<target else search(temp, left, mid, target)

        temp = []
        for num in nums:
            pos = search(temp, 0, len(temp), num)
            if pos >=len(temp):
                temp.append(num)
            else:
                temp[pos]=num
        return len(temp)

test = Solution()
test.lengthOfLIS1([10,9,2,5,3,7,101,18])