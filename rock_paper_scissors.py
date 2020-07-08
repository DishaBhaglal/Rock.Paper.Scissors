#IMPORTING MODULES
from tkinter import*
import random

#MAIN GAME WINDOW
root=Tk()

root.title("Rock Paper Scissors")
root.resizable(width=False,height=False) 
root.configure(bg='DodgerBlue2')

click= True

#STORING IMAGES IN VARIABLES
mainPhoto = PhotoImage(file='main1.png')
rockPhoto = PhotoImage(file='rock1.png') 
paperPhoto = PhotoImage(file='paper1.png')
scissorsPhoto = PhotoImage(file='scissors1.png')

rockPhoto1 = PhotoImage(file='rock1.png')
paperPhoto1 = PhotoImage(file='paper1.png')
scissorsPhoto1 = PhotoImage(file='scissors1.png')

winPhoto = PhotoImage(file='you_win.png')
losePhoto = PhotoImage(file='you_lose.png')
tiePhoto = PhotoImage(file='aargh.png')
tryAgainPhoto = PhotoImage(file='try_again.png')

#BUTTONS AND LABELS
rockButton = ''
paperButton = ''
scissorsButton = ''
mainLabel = ''
tryAgainButton = ''
youLabel = ''
compLabel = ''


def play():
	global rockButton,paperButton,scissorsButton,youLabel,compLabel,tryAgainButton

	rockButton = Button(root, image=rockPhoto,command=lambda:youPick('rock'))
	paperButton = Button(root, image=paperPhoto,command=lambda:youPick('paper'))
	scissorsButton = Button(root, image=scissorsPhoto,command=lambda:youPick('scissors'))
	tryAgainButton = Button(root, image=tryAgainPhoto, command=tryAgain, bg="DodgerBlue2", border=0)
	mainLabel = Label(root, text="Rock.Paper.Scissors ", font=("Verdana",45,"bold"), fg="white", bg="DodgerBlue2")
	youLabel = Label(root, text="Your Choice ", font=("Helvetica",18,"bold"), fg="white", bg="DodgerBlue2")
	compLabel =  Label(root, text="Computer's Choice ", font=("Helvetica",18,"bold"), fg="white", bg="DodgerBlue2")

	mainLabel.grid(row=0, column=0, columnspan=3, pady=30)
	rockButton.grid(row=2, column=0, padx=30, pady=30)
	paperButton.grid(row=2, column=1, padx=30, pady=30)
	scissorsButton.grid(row=2, column=2, padx=30, pady=30)
	

#DETERMINING COMPUTER'S CHOICE
def computerPick():
	choice = random.choice(['rock','paper','scissors'])
	return choice

#MAIN FUNCTION FOR RUNNING THE GAME
def youPick(yourChoice):
	global click,tryAgainButton

	compPick = computerPick()

	youLabel.grid(row=1, column=0)
	compLabel.grid(row=1, column=2) 

	if click == True:
		if yourChoice == 'rock':
			rockButton.configure(image = rockPhoto1)
			if compPick == 'rock':
				paperButton.configure(image = tiePhoto)
				scissorsButton.configure(image = rockPhoto1)
				tryAgainButton.grid(row=3, column=1)
				click = False
			elif compPick == 'paper':
				paperButton.configure(image = losePhoto)
				scissorsButton.configure(image = paperPhoto1)
				tryAgainButton.grid(row=3, column=1)
				click = False	
			else:
				paperButton.configure(image = winPhoto)
				scissorsButton.configure(image = scissorsPhoto1)
				tryAgainButton.grid(row=3, column=1)
				click = False	
		elif yourChoice	== 'paper':
			rockButton.configure(image = paperPhoto1)
			if compPick == 'rock':
				paperButton.configure(image = winPhoto)
				scissorsButton.configure(image = rockPhoto1)
				tryAgainButton.grid(row=3, column=1)
				click = False	
			elif compPick == 'paper':
				paperButton.configure(image = tiePhoto)
				scissorsButton.configure(image = paperPhoto1)
				tryAgainButton.grid(row=3, column=1)
				click = False	
			else:
				paperButton.configure(image = losePhoto)
				scissorsButton.configure(image = scissorsPhoto1)
				tryAgainButton.grid(row=3, column=1)
				click = False	
		elif yourChoice == 'scissors':
			rockButton.configure(image = scissorsPhoto1)
			if compPick == 'rock':
				paperButton.configure(image = losePhoto)
				scissorsButton.configure(image = rockPhoto1)
				tryAgainButton.grid(row=3, column=1)
				click = False	
			elif compPick == 'paper':
				paperButton.configure(image = winPhoto)
				scissorsButton.configure(image = paperPhoto1)
				tryAgainButton.grid(row=3, column=1)
				click = False
			else:
				paperButton.configure(image = tiePhoto)
				scissorsButton.configure(image = scissorsPhoto1)
				tryAgainButton.grid(row=3, column=1)
				click = False	 			
		
#TRY AGAIN FUNCTION
def tryAgain():
	global click,rockButton,paperButton,scissorsButton,youLabel,compLabel
	rockButton.configure(image = rockPhoto)
	paperButton.configure(image = paperPhoto)
	scissorsButton.configure(image = scissorsPhoto)
	youLabel.grid_forget()
	compLabel.grid_forget()
	click = True

	
play()

root.mainloop() 