https://leetcode.com/problems/queens-that-can-attack-the-king/

**Language:Python**
   
   
    class Solution:
        def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
            queens_positions = set()
            for queen in queens:
                queens_positions.add((queen[0],queen[1]))
            result = []
            directions = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
            for direction in directions:
                attacking_queen = self.getAttackingQueen(queens_positions,king,direction)
                if attacking_queen:
                    result.append([attacking_queen[0],attacking_queen[1]])
            return result
        
        def getAttackingQueen(self,queens_positions,king,direction):
            i = king[0]+direction[0] 
            j = king[1]+direction[1]
            if i >= 0 and i < 8 and j >= 0 and j< 8:
                if (i,j) in queens_positions:
                    return (i,j)
            else:
                return None
            return self.getAttackingQueen(queens_positions,[i,j],direction)