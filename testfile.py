def check_sudoku(grid):
	goodVals=[1,2,3,4,5,6,7,8,9]
	#check rows
	for row in grid:
		for vals        in      goodVals:
			# print(str(row)+"\n"+str(vals))
			if      vals not in row:
				print(str(row)+"\n"+str(vals)+"\n")
				print("row issue")
				return False
		checklist=[]
	
	for  col in     range(9):
		for row in      range(9):
			checklist.append(grid[row][col])
			#print(grid[row][col])
		checklist.sort()
		if      checklist!=goodVals:
			#print(str(checklist)+"row "+str(row) +"col "+str(col))
                        return False
		checklist=[]
	return True

def main():
	 grid = [[1,2,3, 4,5,6, 7,8,9],
                            [4,5,6, 7,8,9, 1,2,3],
                            [7,8,9, 1,2,3, 4,5,6],

                            [2,3,4, 5,6,7, 8,9,1],
                            [5,6,7, 8,9,1, 2,3,4],
                            [8,9,1, 2,3,4, 5,6,7],

                            [3,4,5, 6,7,8, 9,1,2],
                            [6,7,8, 9,1,2, 3,4,5],
                            [9,1,2, 3,4,5, 6,7,8],
                           ]
	 print(check_sudoku(grid))

main()
