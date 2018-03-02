class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # Just checking if the board is none or not.
        if len(board) == 0 and len(board[0]) == 0:
            return 0
        # how many ships we can find
        count = 0
        # big thing to remember about this one, is that we are going to never run into invalid ship configs
        # that is a whole different ball game
        # navigate through the rows
        for i in xrange(len(board)):
            # navigate through cols
            for j in xrange(len(board[0])):
                # lets pick this apart
                # 1. We find an x on the board, indicating a ship
                # 2. We check:
                #   2.1. If we are on the 0 col (i == 0)
                #   2.2. We check that the row above is a "." indicating not a ship.
                # 3. We check:
                #   3.1. We are are on the zeroth column, (j == 0)
                #   3.2. The board piece above is water, not a board.
                # 4. If we complete both of those checks, and the current piece on the board is 
                if board[i][j] == 'X' and (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'):
                        count += 1
        return count