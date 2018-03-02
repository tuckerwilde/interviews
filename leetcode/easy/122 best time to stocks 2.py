class Solution(object):
    def maxProfit(self, prices):
        """
        This problem is actually pretty dumb. More than likely, any interview would use # 1
        :type prices: List[int]
        :rtype: int
        """
        # Our return value
        ret = 0
        # Just a sanity check
        if prices:
            # Start with the first value
            start = prices[0]
            # That was our purchase value, which we are forced to make, kinda...
            for i in prices[1:]:
                # Then, moving on from the first point!
                # If our buy price is less than a sell price, SELL! Make profit.
                if start < i:
                    # Add that profit.
                    ret += i - start
                # Move our possible buy point!
                start = i
        # Return that profit, baby.
        return ret
