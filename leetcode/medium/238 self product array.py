class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # This multiplier is what's is keeping tracking behind our iterator
        multiplier = 1
        # This return array is simply the product of self
        # It's doing two things, it's keeping track of left, or everything multiplied to the left of iterators
        # And then going back and multiplying by everything to the right
        ret = [1] * len(nums)

        # Our first iteration through, we are creating a multiplier that is keeping track of everything to the left
        # Placing that into our ret array
        for i in range(len(nums)):
            # At each specific space in our return array, keep track of the multiplier for each value
            ret[i] = ret[i] * multiplier
            # Multiplier gets updated every step
            multiplier = nums[i] * multiplier

        # Drop the multiplier back to one because we are now going to the right
        multiplier = 1
        # Iterate through, starting at the right and going to the left.
        for i in range(len(nums) - 1, -1, -1):
            # Doing the same thing as before.
            ret[i] = ret[i] * multiplier
            multiplier = nums[i] * multiplier
        return ret
