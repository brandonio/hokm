import random

class Card:
	suit = ""
	val = 0

	def __init__(self, suit, val):
		self.suit = suit
		self.val = val

	def __str__(self):
		string = ""
		if self.val > 9:
			string = str(self.val)
		else:
			string = "0" + str(self.val)
		return string + self.suit

deck = []
suits = ["\u2663", "\u2660", "\u2665", "\u2666"]
for s in suits:
	for i in range(2, 15):
		deck.append(Card(s, i))

random.shuffle(deck)

for i in deck:
	print(i)