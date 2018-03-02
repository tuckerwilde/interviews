class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # A simple check to see if we have an empty matrix.
        if not matrix:
            return []
        # These are our descriptors for where we are in the matrix
        row_s = 0
        row_e = len(matrix) - 1
        col_s = 0
        col_e = len(matrix[0]) - 1
        # Our return array, which we are placing all of our values in
        arr = []
        # The iterator we are using to keep track of everything
        i = 0

        while row_s <= row_e and col_s <= col_e:

            # Traverse across a row, starting at col_s and ending at col_e
            # Once it is done, we increment in row_s because we appended the top row
            i = col_s
            while i <= col_e:
                arr.append(matrix[row_s][i])
                i += 1
            row_s += 1

            # Traverse down the right column, starting at row_s and ending at row_e
            # Decrement col_e, we appended the outside column
            i = row_s
            while i <= row_e:
                arr.append(matrix[i][col_e])
                i += 1
            col_e -= 1

            # This is where it gets trick with checks, we need to make sure we aren't overlapping things.
            # Starting at the col_e, we work our way into the col_s
            i = col_e
            if row_s <= row_e:
                while i >= col_s:
                    arr.append(matrix[row_e][i])
                    i -= 1
            row_e -= 1

            # Another odd check, but nothing can be done.
            # Starting at row_e we work our way up to row_s
            # Incrementing col_s
            i = row_e
            if col_s <= col_e:
                while i >= row_s:
                    arr.append(matrix[i][col_s])
                    i -= 1
            col_s += 1

        return arr


    def spiralOrderTwo(self, matrix):
        # the craziest fucking one liner for this bitch.
        """
        |1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
        |4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
        |7 8 9|      |4 7|
        Zip essentially transposes a matrix on itself. I guess.
        :param matrix:
        :return:
        """
        return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])