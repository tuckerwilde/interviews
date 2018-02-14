class Solution(object):
    stack = [[1], [1, 1]]
    """
    This is my method, it is pretty bare but it passes all the test cases.
    Time: O(M * N), M is the numbers from 0-numRows, N is the arrays for each of those numbers being generated
    Space: (not including return value) O(M * N)
    """

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        ret = []
        for i in xrange(numRows):
            # Try to access our stack of numbers, if not then it needs to be created.
            try:
                ret.append(self.stack[i])
            # Lets create the array and append it to everything.
            except:
                # The arrays with always start with 1.
                temp = [1]
                # Starting at the 2nd position, index 1, in the previous array we build
                # For example, for the 3rd row, we access the second row which is a base case
                # [1, 2, 1] = [1]-> append([1] + [0]) -> [1,2]
                for j in xrange(1, len(self.stack[i - 1])):
                    temp.append(self.stack[i - 1][j - 1] + self.stack[i - 1][j])
                # As well, it's always guaranteed to have a 1 at the end. So: [1,2].append(1) -> [1,2,1]
                temp.append(1)
                # Append that to our stack for DP
                self.stack.append(temp)
                # Append to our return value.
                ret.append(temp)
        return ret

    """
    This method is pulled off of leetcode, https://leetcode.com/problems/pascals-triangle/discuss/38136/A-simple-python-solution.
    Just going through to see a shorter, simpler solution.
    """

    def generate2(self, numRows):
        # Our return value.
        lists = []
        # Let's build each step.
        for i in range(numRows):
            # This will fill a row up with as many 1s as necessary.
            # For example, i == 3 -> [1,1,1,1]. The fourth row -> i == 3 -> thus four integers in that row.
            lists.append([1] * (i + 1))
            # If it's not zero, which is just [1].
            if i > 1:
                # Continuing our example from before. from 1->3.
                for j in range(1, i):
                    # Utilizes the last array, just as I did. Summing them up and placing it.
                    # This is better because it doesn't have to do the stupid append(1).
                    lists[i][j] = lists[i - 1][j - 1] + lists[i - 1][j]
        return lists
