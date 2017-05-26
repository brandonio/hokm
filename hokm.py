import random, time

suits = ["\u2663", "\u2660", "\u2665", "\u2666"]
sc = ["s", "c", "d", "h"]

etc = {"\u2663": "c", "\u2660": "s", "\u2665": "h", "\u2666": "d"}
cte = {"c": "\u2663", "s": "\u2660", "h": "\u2665", "d": "\u2666"}
lets = ["a", "k", "q", "j", "x"]

class Game:
	hio = True

	def __init__(self, p1, p2, deck):
		self.p1 = p1
		self.p2 = p2
		self.deck = deck
		self.r = 1
		self.hio = self.h()
		self.hokm = ""

	def lego(self):
		self.p1.addCards(self.deck.d[:6])
		self.p2.addCards(self.deck.d[6:12])

	def rn(self):
		return self.r

	def setHokm(self, s):
		self.hokm = s

	def hakem(self):
		if self.hio:
			return self.p1
		else:
			return self.p2

	def nonhak(self):
		if self.hio:
			return self.p2
		else:
			return self.p1

	def h(self):
		print("We will now flip cards to determine who is going to be the Hakem.")
		print(self.p1.name + " gets the first card and we will continue from there.")
		x = 0
		c = ""
		for i in range(52):
			c = self.deck.cai(i)
			if x % 2 == 0:
				print(self.p1.name + "'s card:")
			else:
				print(self.p2.name + "'s card:")
			c.printfull()
			if c.val == 14:
				break
			# time.sleep(.65)
			p(4)
			x += 1
		print("Our first Ace! ", end="")
		self.hio = x % 2 == 0
		if self.hio:
			print(self.p1.name + " will be the first Hakem.")
		else:
			print(self.p2.name + " will be the first Hakem.")
		return x % 2 == 0

	def sethio(self, b):
		self.hio = b

	def hio(self):
		return self.hio

	def changeHakem(self):
		self.hio = not self.hio

	def isWinner(self):
		if self.p1.games == 7 or self.p2.games == 7:
			self.r += 1
			return True
		else:
			return False
	
	def handone(self):
		if self.p1.hands == 7 or self.p2.hands == 7:
			self.p1.reset()
			self.p2.reset()
			self.hokm = ""
			return True
		else:
			return False

	def handWinner(self):
		b = True
		if self.p1.hands == 7:
			print(self.p1.name + " won this hand!")
			self.p1.win()
		else:
			b = False
			print(self.p2.name + " won this hand!")
			self.p2.win()
		if not self.isWinner():
			print("The score is:")
			print(self.p1.name + ": " + str(self.p1.games))
			print(self.p2.name + ": " + str(self.p2.games))
			if b:
				if self.hio:
					print(self.p1.name + " will remain the Hakem.")
				else:
					self.changeHakem()
					print(self.p2.name + " will now be the Hakem.")
			else:
				if not self.hio:
					print(self.p2.name + " will remain the Hakem.")
				else:
					self.changeHakem()
					print(self.p1.name + " will now be the Hakem.")
		else:
			self.whoWon()

	def whoWon(self):
		print("The game is now over!")
		print("After " + str(self.r) + " rounds, we have a winner!")
		if self.p1.games() == 7:
			print("Congratulations to " + self.p1.name + " for winning!")
		else:
			print("Congratulations to " + self.p2.name + " for winning!")

class Deck:
	d = []

	def __init__(self):
		for s in suits:
			for i in range(2, 15):
				self.d.append(Card(s, i))
		random.shuffle(self.d)

	def cai(self, i):
		return self.d[i]

	def shuffle(self):
		d = random.shuffle(d)


class Card:
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
	def __eq__(self, other):
	    if isinstance(other, self.__class__):
	        if self.c == other.c and self.suit == other.suit:
	        	return True
	        else:
	        	return False
	    else:
	    	return False

	def __str__(self):
		return self.c + self.suit

	def printleft(self):
		ul("    ")
		print("|")
		print("|", end="")
		print(self)
		ul("|   ")

	def printfull(self):
		ul("      ")
		print("|    |")
		# print("|    |")
		print("| ", end="")
		print(self, end="")
		if self.val != 10:
			print(" |")
		else:
			print("|")
		print("|    |")
		ul("|    |")

	def printright(self):
		ul("    ")
		print("   |")
		print(self, end="")
		if self.val != 10:
			print(" |")
		else:
			print("|")
		ul("   |")

class Player:
	def __init__(self, name):
		self.name = name
		self.hands = self.games = 0
		self.cards = []

	def reset(self):
		self.hands = 0

	def gn(self, n):
		for c in self.cards:
			if c.val == n:
				return c
		print("THIS SHOULD NEVER PRINT!")
		return None

	def remove(self, c):
		self.cards.remove(c)
		print("Your new hand is:")
		self.pc()
		return c

	def getint(self, s):
		if "x" in s:
			return 10
		if "a" in s:
			return 14
		if "k" in s:
			return 13
		if "q" in s:
			return 12
		if "j" in s:
			return 11
		return int(s)

	def throw(self):
		# lst = []
		first = True
		while len(self.cards) > 3:
			if not first:
				print("Remember: ", end="")
			print("You have to throw away " + str(len(self.cards) - 3) + " cards.")
			if first:
				first = False
				print("You can enter multiple cards at once by separating them with spaces.")
			t = input().lower().strip()
			t = t.replace("x", "")
			t = t.replace("10", "x")
			lst = t.split(" ")
			if len(lst) < 1:
				print("You have to enter at least one card. ", end="")
				continue
			if len(lst) > 3:
				print("You have entered too many cards. ", end="")
				continue
			if len(self.cards) - len(lst) < 3:
				print("You are trying to throw away too many cards. ", end="")
				continue
			for i, l in enumerate(lst):
				val = self.getint(l[0])
				if len(l) > 2 or len(l) < 1 or not (l[0].isdigit() or l[0] in lets):
					print("Your" + self.ntp(i) + "entry was not formatted correctly.")
				elif len(l) == 1:
					if self.numnum(val) == 0:
						print("You do not have a " + str(val) + " in your hand.")
					elif self.numnum(val) > 1:
						print("You have more than one " + str(val) + " in your hand.")
						print("Please enter a value AND a suit when this is the case.")
					else:
						c = self.gn(val)
						print("Your " + str(c) + " will be deleted.")
						self.remove(c)
				else:
					if l[1].isdigit() or l[1] not in cte.keys():
						print("Your" + self.ntp(i) + "entry was not formatted correctly.")
					else:
						c = Card(cte[l[1]], val)
						if self.hascard(c):
							print("Your " + str(c) + " will be deleted.")
							self.remove(c)
						else:
							print("You do not have a " + l + " in your hand.")

	def ntp(self, n):
		if n == 0:
			return " first "
		if n == 1:
			return " second "
		if n == 2:
			return " third "

	def hassuit(self, s):
		suit = cte[s]
		for c in self.cards:
			if c.suit == suit:
				return True
		return False

	def hascard(self, x):
		# x = Card(cte[s[1]], int(s[0]))
		for c in self.cards:
			if c.val == x.val and c.suit == x.suit:
				return True
		return False

	def numnum(self, n):
		x = 0
		for c in self.cards:
			if c.val == n:
				x += 1
		return x

	def numsuit(self, s):
		x = 0
		suit = cte[s]
		for c in self.cards:
			if c.suit == suit:
				x += 1
		return x

	def hasnum(self, n):
		for c in self.cards:
			if c.val == n:
				return True
		return False

	def win(self):
		self.games += 1

	def addCard(self, card):
		self.cards.append(card)

	def addCards(self, lst):
		self.cards.extend(lst)

	def pc(self):
		if len(self.cards) == 0:
			print("You do not have any cards.")
			return
		if len(self.cards) == 0:
			self.cards[0].printfull()
			return
		print(self.name + ", here are your cards:")
		for _ in self.cards:
			ulnl("      ")
			print("  ", end="")
		print()
		print("|    |  " * len(self.cards))
		for c in self.cards:
			print("| ", end="")
			print(c, end="")
			if c.val != 10:
				print(" |  ", end="")
			else:
				print("|  ", end="")
		print()
		print("|    |  " * len(self.cards))
		for _ in self.cards:
			ulnl("|    |")
			print("  ", end="")
		p(2)

	# def handle(self, s):

	def ch(self, game):
		x = input("What suit do you want to be Hokm...").lower().strip()
		while len(x) != 1 or x not in sc:
			print("Please enter one of the following: ", end="")
			print(str(list(sc))[1:len(str(list(sc))) - 1])
			x = input("What suit do you want to be Hokm...").lower().strip()
		#get suit using char (dictionary)
		print("Got it! Hokm will be" + gfn(x) + cte[x] + ".")
		game.setHokm(x)

	

def gfn(s):
	if s == "s":
		return " Spades "
	if s == "h":
		return " Hearts "
	if s == "c":
		return " Clovers "
	if s == "d":
		return " Diamonds "

def ul(*args, **kwargs):
	print("\033[4m"+args[0]+"\033[0m")

def ulnl(*args, **kwargs):
	print("\033[4m"+args[0]+"\033[0m", end="")

def p(x=1):
	for i in range(x):
		print()

def info():
	print("Welcome to Brandon's Two-Player Hokm!")
	print("-------------------------------------")
	print("How To Play:")
	print("'6c' means you want to play a 6 of Clovers. The same goes for Spades, Hearts, and Diamonds, using 's', 'h', and 'd,' respectively.")
	print("If you have only one 6 in your hand, you can simply enter '6' and that card will be played.")
	input("Press enter once you understand how to play a card...")


def start():
	info()
	p1 = Player(input("What is the name of the first player?\n").title())
	p2 = Player(input("What is the name of the second player?\n").title())
	deck = Deck()
	g = Game(p1, p2, deck)
	while not g.isWinner():
		if g.rn() != 1:
			print(g.hakem().name + " is the Hakem for round " + str(g.rn()))
		print("Let's begin!")
		g.lego()
		print(g.hio)
		print(g.hio)
		print(g.hio)
		print(g.hio)
		print(g.hio)
		print(g.nonhak().name + ", please look away.")
		input(g.hakem().name + ", press enter to show your cards...")
		g.hakem().pc()
		g.hakem().ch(g)
		g.hakem().throw()
		input("Press enter when you are done...")
		p(62)
		print(g.hakem().name + ", please look away.")
		input(g.nonhak().name + ", press enter to show your cards...")
		g.nonhak().pc()
		g.nonhak().throw()
		input("Press enter when you are done...")
		p(62)
		# g.distribute()
		break

start()

























