def rob(num):
    max_3_house_before, max_2_house_before, adjacent = 0, 0, 0
    for cur in num:
        """
        The way this currently sits, it will not work.
        It must be one-line, so that there isn't calculations on later numbers.
        """
        # This is a sliding window of 4. Initially set to [0,0,0,num[0]]
        # max_3_house_before: stores the maximum sum until the house 3 steps before the current (cur).
        # max_3_house_before = max_2_house_before
        # max_2_house_before: stores the maximum sum until the house 2 steps before the current (cur).
        # max_2_house_before = adjacent
        # adjacent: stores the maximum sum until the house 1 step before the current (cur).
        # to reach our current house, we either came from the house three steps before, or two steps before
        # this is because of the limitation set out, where we cannot rob two adjacent houses.
        # adjacent = max(max_3_house_before + cur, max_2_house_before + cur)
        max_3_house_before, max_2_house_before, adjacent = \
            max_2_house_before, adjacent, max(max_3_house_before+cur, max_2_house_before+cur)


    # This reflects that limitation, we either do the two steps before, or the single step before.
    return max(max_2_house_before, adjacent)


print rob([1, 7, 9, 4])