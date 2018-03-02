class Solution(object):
    def firstUniqChar(self, s):
        from collections import Counter
        """
        :type s: str
        :rtype: int
        """
        # Utilizing what is essentially a high frequency dictionary. Easier to use.
        counts = Counter(s)
        # After initializing, we have the counts of each letter in that dictionary.
        for i in range(len(s)):
            # Run through, the first one we see in the string with a count of 1, then we kickback
            if counts[s[i]] == 1:
                # We return the index of the first one
                return i
        # If we can't find a single character, then kickback -1
        return -1

    def two_firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # This value is arbitrary, essentially saying outside the max length of string... or whatever.
        MIN = 1999999999
        # This is essentially assuming all the values in the string fall into this holder string
        ab = "abcdefghijklmnopqrstuvwxyz"
        # iterate through our string of characters
        for x in ab:
            # Look for the first index of each character
            idx = s.find(x)
            # If it's in the string, I.E. not equal to -1
            if idx != -1:
                # We do a right find! This is essentially finding the last index of the character
                if idx == s.rfind(x):  # ONLY ONCE
                    # So we know now that the indices match! Meaning, there is only one of the characters
                    # Then we check if that index is the smallest we've found thus far.
                    if idx < MIN:
                        MIN = idx
        # If we still have that arbitrary value, kick back -1, otherwise return the indices.
        return -1 if MIN == 1999999999 else MIN
