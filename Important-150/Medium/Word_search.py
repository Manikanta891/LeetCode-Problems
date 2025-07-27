# Definition:
# Given a 2D board and a word, check if the word exists in the board.
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get dimensions of the board
        rows, cols = len(board), len(board[0])

        # Initialize visited matrix to keep track of used cells
        visited = [[False]*cols for _ in range(rows)]

        # Recursive helper function to perform DFS search
        def search(i, j, pos):
            # If we have matched all characters in the word
            if pos == len(word):
                return True

            # Check for invalid index, already visited, or mismatch
            if (i < 0 or i >= rows or j < 0 or j >= cols or
                visited[i][j] or board[i][j] != word[pos]):
                return False

            # Mark current cell as visited
            visited[i][j] = True

            # Explore all 4 adjacent directions (up, down, left, right)
            res = (search(i+1, j, pos+1) or
                   search(i-1, j, pos+1) or
                   search(i, j+1, pos+1) or
                   search(i, j-1, pos+1))

            # Backtrack and unmark the cell
            visited[i][j] = False
            return res

        # Try to find the word starting from each cell in the board
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and search(i, j, 0):
                    return True

        # If no path matched the word
        return False



# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         cols=len(board[0])
#         rows=len(board)
#         visited = [[False]*cols for _ in range(rows)]
#         def search(i,j,word):
#             if board[i][j]==word[0] and len(word)==1:
#                 return True
#             if board[i][j]==word[0]:
#                 visited[i][j]=True
#                 a=b=c=d=False
#                 if 0<=i+1<rows and  0<=j<cols and not visited[i+1][j]:
#                     a=search(i+1,j,word[1:])
#                 if 0<=i<rows and  0<=j+1<cols and not visited[i][j+1]:
#                     b=search(i,j+1,word[1:])
#                 if 0<=i-1<rows and  0<=j<cols and not visited[i-1][j]:
#                     c=search(i-1,j,word[1:])
#                 if 0<=i<rows and  0<=j-1<cols and not visited[i][j-1]:
#                     d=search(i,j-1,word[1:])
#                 visited[i][j]=False
#                 return a or b or c or d

#             else:
#                 return False
#         for i in range(rows):
#             for j in range(cols):
#                 res=search(i,j,word)
#                 if res:
#                     return True
#         return False

# Passing the string every time take memory better send the position
