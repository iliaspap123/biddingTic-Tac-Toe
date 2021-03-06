from graphics import *
from Actions import *
import math

class Player:


	def __init__(self,shape,marks,name):
		self.shape = shape
		self.marks = marks
		self.name = name

	def play(self,row,col,table):
		return table.insertMove(row,col,self.shape)

class Table:

	def __init__(self):
		self.listPos = [[' ']*3,[' ']*3,[' ']*3]

	def printTable(self):
		''' prints tic tac toe in terminal '''
		print(' '+ self.listPos[0][0]+' | '+self.listPos[0][1]+' | '+self.listPos[0][2])
		print('-----------')
		print(' '+ self.listPos[1][0]+' | '+self.listPos[1][1]+' | '+self.listPos[1][2])
		print('-----------')
		print(' '+ self.listPos[2][0]+' | '+self.listPos[2][1]+' | '+self.listPos[2][2] + '\n')


	def insertMove(self,row,col,shape):
		if row > 2 or col > 2:
			return False
		if self.listPos[row][col] != ' ':
			return False
		self.listPos[row][col] = shape
		return True

	def isWinnigState(self):
		for i in range(3):
			if(self.listPos[i][0] == self.listPos[i][1] == self.listPos[i][2] != ' '):
				return(True)
			if(self.listPos[0][i] == self.listPos[1][i] == self.listPos[2][i] != ' '):
				return(True)
		if(self.listPos[0][0] == self.listPos[1][1] == self.listPos[2][2] != ' '):
				return(True)
		if(self.listPos[0][2] == self.listPos[1][1] == self.listPos[2][0] != ' '):
				return(True)
		return(False)

def draw(win,center,shape):
	''' graphics: draw 'X' or 'O' '''
	if(shape == 'X'):
		x,y = center.x , center.y
		X1 = Line(Point(x-10,y-10),Point(x+10,y+10))
		X2 = Line(Point(x-10,y+10),Point(x+10,y-10))
		X1.setFill('red')
		X2.setFill('red')
		X1.setWidth(1)
		X1.draw(win)
		X2.draw(win)
	else:
		circle = Circle(center,15)
		circle.setOutline('blue')
		circle.setWidth(1)
		circle.draw(win)

def get_box(px,py):
	''' takes cordinates px,py and returns the box indexes and the center in graphics '''
	linesize = 200/3
	if(px > 50 and px <= 50+linesize and py > 50 and py <= 50+linesize ):
		return (0,0,Point(50+(linesize/2),50+(linesize/2)))

	if(px > 50+linesize and px <= 50+(2*linesize) and py > 50 and py <= 50+linesize ):
		return (0,1,Point(50+(3*linesize/2),50+(linesize/2)))

	if(px > 50+(2*linesize) and px <= 250 and py > 50 and py <= 50+linesize ):
		return (0,2,Point(150+linesize,50+(linesize/2)))

	if(px > 50 and px <= 50+linesize and py > 50+linesize and py <= 50+(2*linesize) ):
		return (1,0,Point(50+(linesize/2),50+(3*linesize/2)))

	if(px > 50+linesize and px <= 50+(2*linesize) and py > 50+linesize and py <= 50+(2*linesize) ):
		return (1,1,Point(50+(3*linesize/2),50+(3*linesize/2)))

	if(px > 50+(2*linesize) and px <= 250 and py > 50+linesize and py <= 50+(2*linesize) ):
		return (1,2,Point(150+linesize,50+(3*linesize/2)))

	if(px > 0 and px <= 50+linesize and py > 50+(2*linesize) and py <= 250 ):
		return (2,0,Point(50+(linesize/2),150+linesize))

	if(px > 50+linesize and px <= 50+(2*linesize) and py > 50+(2*linesize) and py <= 250 ):
		return (2,1,Point(50+(3*linesize/2),150+linesize))

	if(px > 50+(2*linesize) and px <= 250 and py > 50+(2*linesize) and py <= 250 ):
		return (2,2,Point(150+linesize,150+linesize))

	return (10,10,Point(150,150))

def get_center(i,j):
	''' takes cordinates px,py and returns the box indexes and the center in graphics '''
	linesize = 200/3
	if(i == 0 and j == 0 ):
		return Point(50+(linesize/2),50+(linesize/2))

	if(i == 0 and j == 1 ):
		return Point(50+(3*linesize/2),50+(linesize/2))

	if(i == 0 and j == 2 ):
		return Point(150+linesize,50+(linesize/2))

	if( i == 1 and j == 0 ):
		return Point(50+(linesize/2),50+(3*linesize/2))

	if( i == 1 and j == 1 ):
		return Point(50+(3*linesize/2),50+(3*linesize/2))

	if( i == 1 and j == 2 ):
		return Point(150+linesize,50+(3*linesize/2))

	if( i == 2 and j == 0 ):
		return Point(50+(linesize/2),150+linesize)

	if( i == 2 and j == 1 ):
		return Point(50+(3*linesize/2),150+linesize)

	if( i == 2 and j == 2 ):
		return Point(150+linesize,150+linesize)

	return Point(150,150)

def main():

	''' Graphics '''
	windowsize = 300
	linesize = 200
	squares = 3
	boxsize = 100

	win = GraphWin("Tic Tac Toe", windowsize, windowsize)

	for i in range(squares - 1):
		hline = Line(Point(50,50 +((linesize/squares) * (i + 1))), Point(linesize+50, 50 + ((linesize/squares) * (i + 1))))
		hline.draw(win)
		vline = Line(Point(50 + ((linesize/squares) * (i + 1)), 50), Point(50 + ((linesize/squares) * (i + 1)), 50 + linesize))
		vline.draw(win)

	textEntryP1 = Entry(Point(50,20),5)
	textEntryP1.setFill("white")
	textEntryP1.draw(win)
	textEntryP2 = Entry(Point(250,20),5)
	textEntryP2.setFill("white")
	textEntryP2.draw(win)
	''' '''

	''' Initialize '''
	player1 = Player('X',100,'player1')
	player2 = Player('O',100,'player2')
	print(player1.shape,player1.marks)

	table = Table()
	print(table.listPos)
	table.printTable()
	''' '''

	# graphics print marks number
	showMarks1 = Text(Point(90, 20), player1.marks)
	showMarks1.draw(win)
	showMarks2 = Text(Point(210, 20), player2.marks)
	showMarks2.draw(win)


	i = 0
	agent = MinimaxAgent() # initialize agent
	while i < 9:

		(res,pos) = agent.getAction2(table.listPos) # find best bet and move
		if res*200 <= player2.marks: # if have enough marks
			print("I have a winnig strategy",player2.marks,"over",(res*200))
			bidP2 = math.floor((abs(agent.tmp1-agent.tmp2)/2) * 200)
		else:
			if agent.tmp2 == 1: # if next move is final
				bidP2 = player1.marks+1
			else:
				minus = math.ceil((res*200 - player2.marks)/2)
				bidP2 = math.floor((abs(agent.tmp1-agent.tmp2)/2) * 200) - minus
			print((res*200),"not yet",player2.marks,"    ",minus)
		print('Current marks player1: ',player1.marks,'  player2: ',player2.marks)

		''' get valid entry '''
		k = win.getKey() # wait for players move
		while  k != 'Return':
			k = win.getKey()

		str_int = textEntryP1.getText()
		while not str_int.isdigit():
			print("please type integer")
			k = win.getKey()
			while  k != 'Return':
				k = win.getKey()
			str_int = textEntryP1.getText()

		bidP1 = int(str_int)

		if(bidP2 > player2.marks):
			bidP2 = player2.marks





		if bidP1 > player1.marks or bidP2 > player2.marks:
			continue

		textEntryP2.setText(bidP2)
		if bidP1 > bidP2:
			player = player1
			player1.marks -= bidP1
			player2.marks += bidP1

			print(player.name,'plays')
			showMarks1.setText(player1.marks)
			showMarks2.setText(player2.marks)
			flag = True
			while flag:
				p1mouse = win.getMouse()
				print(p1mouse.getX(), p1mouse.getY())
				row,col,c = get_box(p1mouse.getX(),p1mouse.getY())
				print(row,col)
				#row = int(input("Enter a row: "))
				#col = int(input("Enter a column: "))
				if player.play(row,col,table):
					draw(win,c,player.shape)
					table.printTable()
					i+=1
					flag = False
				else:
					print("illegal move")

		else:
			player = player2
			player2.marks -= bidP2
			player1.marks += bidP2
			#(row,col) = agent.getAction(table.listPos,'O','X')
			(row,col) = pos
			c = get_center(row,col)
			print(player.name,'plays')
			showMarks1.setText(player1.marks)
			showMarks2.setText(player2.marks)
			if player.play(row,col,table):
				draw(win,c,player.shape)
				table.printTable()
				i+=1
				flag = False
			else:
				print("illegal move")

		if table.isWinnigState():
			print("we have a winner")
			break



	table.printTable()
	win.close()




main()
