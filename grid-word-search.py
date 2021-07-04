class WordSearch:

    def __init__(self,grid):

        self.grid=grid
        self.directions = [[0,-1],[-1,0],[0,1],[1,0]]
        self.R = len(grid)
        self.C = len(grid[0])
        print(self.grid)

    def searchWord(self,word,row,col,position):

        # print(word,position,word[position],row,col)

        if row<0 or row>=self.R or col<0 or col>=self.C:
            return False

        if position == len(word):
            return True


        if word[position] == self.grid[row][col]:

            result = (self.searchWord(word,row,col-1,position+1) or 
                        self.searchWord(word,row-1,col,position+1) or
                        self.searchWord(word,row,col+1,position+1) or
                        self.searchWord(word,row+1,col,position+1))

            return result
        else:
            return False

        return True

    

if __name__=="__main__":

    grid = [['a','x','m','y'],
                ['b','e','e','f'],
                ['x','e','e','f'],
                ['r','a','k','s']]

    search = WordSearch(grid)
    word = input()
    wordFound = False

    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if word[0] == grid[i][j]:
                if search.searchWord(word,i,j,0):
                    print("Word found at {i},{j}".format(i=i,j=j))
                    wordFound = True
                    break

    if not wordFound:

        print("Word not found")

    