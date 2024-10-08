class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False
    
    def dfs(self, board, word, i, j, s):
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]): # out of bounds
            return False
        if board[i][j] != word[s] or board[i][j] == "*": # current cell not matching current character of word, or visited before
            return False
        if s == len(word) - 1: # current position reached end of word
            return True
        
        cache = board[i][j] # saving original board layout
        board[i][j] = "*"
        exists = self.dfs(board, word, i + 1, j, s + 1) or \
                 self.dfs(board, word, i - 1, j, s + 1) or \
                 self.dfs(board, word, i, j + 1, s + 1) or \
                 self.dfs(board, word, i, j - 1, s + 1)
        board[i][j] = cache # restoring original board layout

        return exists