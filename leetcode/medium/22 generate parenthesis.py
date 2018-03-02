class Solution(object):
    def generateParenthesis(self, N):
        # our return array
        ans = []
        # helper function
        def backtrack(S = '', left = 0, right = 0):
            # in this problem, the max amount of items in our array is going to be 2 * N
            # once one of our current recursed functions get to this point, append and break
            if len(S) == 2 * N:
                ans.append(S)
                return
            # we know that we need to have equal amounts of left and right.
            # so go through with the left, and recurse.
            if left < N:
                backtrack(S+'(', left+1, right)
            # now let's match the left. go through with the recursion of the right side.
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

Solution().generateParenthesis(3)