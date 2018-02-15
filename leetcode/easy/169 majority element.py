class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        This utilizes the algorithm found here:
        http://www.cs.utexas.edu/~moore/best-ideas/mjrty/

        Boyer-Moore Majority Vote Algorithm
        """
        if len(nums) == 1:
            return nums[0]
        else:
            number = nums[0]
            count = 0

            for num in nums:
                if num == number:
                    count += 1
                else:
                    if count == 0:
                        number = num
                        count = 1
                    else:
                        count -= 1
            return number