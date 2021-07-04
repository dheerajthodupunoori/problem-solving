def searchWords (self, grid, words):
	maximum_length = max([len(word) for word in words])
	words = set(words)
	row = len(grid)
	column = len(grid[0])
	valid_directions = [[-1, 0], [1, 0], [1, 1],[1, -1], [-1, -1], [-1, 1],[0, 1], [0, -1]]
	for i in range(row):
		for j in range(column):
			for direction in valid_directions:
                result = generateWord(grid, i, j, maximum_length, words, grid[i][j],direction,set())
                for word in result:
                    print(word,i,j)

def generateWord(self, grid, row, column, maximum_length ,  words, generated_word, direction,result):

    if generated_word in words:

        result.add(generated_word)
    
    if len(generated_word) >= maximum_length:
        return result

    row+=direction [0]
    column+=direction [1]

    if row>=0 and row<len(grid) and column>=0 and column<len(grid[0]):

        generated_word+=grid[row][column]
        return generateWord(grid,row,column,maximum_length,words,generated_word,direction)
