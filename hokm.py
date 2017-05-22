import random

suits = ["\u2663", "\u2660", "\u2665", "\u2666"]

class Deck:
	d = []
	p1wins = p2wins = 0
	n1 = n2 = ""
	p1hands = p2hands = 0

	def __init__(self, n1, n2):
		self.n1 = n1
		self.n2 = n2
		for s in suits:
			for i in range(2, 15):
				d.append(Card(s, i))
		random.shuffle(d)

	def isWinner(self):
		if p1wins == 7 or p2wins == 7:
			return True
		else:
			return False
	
	def handone(self):
		if p1hands == 7 or p2hands == 7:
			return True
		else:
			return False

	def handWinner(self):
		if p1hands == 7:
			if fif:
				p1wins += 1
			else:
				p2wins += 1
		elif p2hands == 7:
			if fif:
				p2wins += 1
			else:
				p1wins += 1

	def whoWon(self):
		if p1wins == 7:
			if fif:
				print("Congratulations! " + n1 + " is the winner!")
			else:
				print("Congratulations! " + n2 + " is the winner!")
		elif p2wins == 7:
			if fif:
				print("Congratulations! " + n2 + " is the winner!")
			else:
				print("Congatulations! " + n1 + " is the winner!")

	class Card:
		suit = ""
		val = 0
		c = ""

		def __init__(self, suit, val):
			self.suit = suit
			self.val = val
			if val < 11:
				self.c = str(val)
			elif val == 11:
				self.c = "J"
			elif val == 12:
				self.c = "Q"
			elif val == 13:
				self.c = "K"
			elif val == 14:
				self.c = "A"

		def __str__(self):
			return self.c + self.suit

		def printleft(self):
			ul("    ")
			print("|")
			print("|", end="")
			print(self)
			ul("|   ")

		def printfull(self):
			ul("       ")
			print("|     |")
			if self.val != 10:
				print("|  ", end="")
			else:
				print("| ", end="")
			print(self, end="")
			print(" |")
			ul("|     |")

		def printright(self):
			ul("    ")
			print("   |")
			print(self, end="")
			if self.val != 10:
				print(" |")
			else:
				print("|")
			ul("   |")

def ul(*args, **kwargs):
	#ignore comment
	print("\033[4m"+args[0]+"\033[0m")

def p(x=1):
	for i in range(x):
		print()

def info():
	print("Welcome to Brandon's Two-Player Hokm!")
	print("-------------------------------------")
	print("How To Play:")
	print("'6 c' means you want to play a 6 of Clovers. The same goes for Spades, Hearts, and Diamonds.")
	print("If you have only one 6 in your hand, you can simply enter '6' and that card will be played.")
	input("Press enter once you understand how to play a card...")


def start():
	info()
	n1 = input("What is the name of the first player?")
	n2 = input("what is the name of the second player?")
	d = Deck(n1, n2)
	
















