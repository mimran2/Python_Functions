def fib(n, val=1,prev=0):
	if	n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fib(n-1,val+prev,val)

def reversed(xs):
	mylist=[xs[len(xs)-1-i]	for i	in	range(len(xs))]
	return mylist

def is_prime(x):
	if	x<2:
		return false
	if	x==2:
		return true
	else:
		for i	in	range(2,x):
			if	x%i==0:
				return False
	return True

def nub(xs):
	mylist=[]
	for i	in	xs:
		if	i not	in	mylist:
			mylist.append(i)
	return mylist

def zip_with(function,x,y):
	rList=[]
	if len(x)==0 or len(y)==0:
		return	rList
	elif	len(x)<=len(y):
		for	i in range(len(x)):
			rList.append(function(x[i],y[i]))
		return	rList	
	elif	len(y)<len(x):
		for	i in range(len(y)):
			rList.append(function(x[i],y[i]))
	return	rList

def collatz(n):
	myList=[]
	myList.append(n)
	while(n!=1):
		if n%2==0:
			n=n/2
		elif(n%2==1):
			n=n*3+1
		myList.append(n)
	return myList

def file_report(filename):
	mylist=[]
	#return mean median mode
	f=open(filename,'r')
	for line	in	f:
		mylist.append(int(line))
	#get mean
	mean=0.0
	for x	in	mylist:
		mean+=x
	mean=mean/len(mylist)
	mylist.sort()
	if(len(mylist)%2==0):
		median=mylist[len(mylist)//2-1]+mylist[len(mylist)//2]+0.0
		median=median/2
	else:
		median=mylist[len(mylist)//2]
	#modefinder
	modelist=[]
	countlist=[]
	for x	in	range(len(mylist)):
		if	mylist[x] not in modelist:
			modelist.append(mylist[x])
			countlist.append(1)
		else:
			countlist[modelist.index(mylist[x])]+=1
	maxVal=max(countlist)
	returnList=[]
	for x	in	range(len(countlist)):
		if	countlist[x]==maxVal:
			returnList.append(modelist[x])
	return (mean,median, returnList)

def check_sudoku(grid):
	goodVals=[1,2,3,4,5,6,7,8,9]
	#for x in grid:
		#print( str(x)+"\n")
	#check rows
	for row in grid:
		for vals	in	goodVals:
			print(str(row)+"\n"+str(vals))
			if	vals not in row:
				#print(str(row)+"\n"+str(vals)+"\n")
				#print("row issue")
				return False
	checklist=[]
		
	for  col in	range(9):
		for row	in	range(9):
			checklist.append(grid[row][col])
			#print(grid[row][col])
		checklist.sort()
		if	checklist!=goodVals:
			#print(str(checklist)+"row "+str(row) +"col "+str(col))
			return False
		
		checklist=[]
	  
	list3=[]	  
	  
	for k	in	range(0,9,3):
		for i	in	range(3):#rows
			for j	in	range(k,k+3):#columns
				list3.append(grid[i][j])
		list3.sort()
		if(list3!=goodVals):
		   print(str(list3)+" range 3")
		   return False
		else:
		   list3=[]
	
	for k   in      range(0,9,3):
		for i   in      range(3,6):#rows
			for j   in      range(k,k+3):#columns
				list3.append(grid[i][j])
		list3.sort()
		if(list3!=goodVals):
			print(str(list3)+" range 3,6")
			return False
		else:
			list3=[]

	for k   in      range(0,9,3):
		for i   in      range(6,9):#rows
			for j   in      range(k,k+3):#columns
				list3.append(grid[i][j])
		list3.sort()
		if(list3!=goodVals):
			print(str(list3)+" range 6,9")
			return False
		else:
			list3=[]


	return True
  #check	next 3x3
  
			
#def make_file(msg,filename="data.txt"):
 #	 f=open(filename,'w')
  # f.write(msg)
  # f.close					
#def main():
  # print(is_prime(61))
  # print(is_prime(43))
  # print(is_prime(601))
  # print(is_prime(51))
 #	 make_file("1\n2\n3\n4\n")
  # print(file_report("data.txt"))
#main()
