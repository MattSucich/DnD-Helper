import random

class Monster(object):
	"""Monster: stores name, description and hit dice for adding mobs to the combat order"""
	def __init__(self, name, dicenum, dicesize, hpmod, desc):
		super(Monster, self).__init__()
		self.name = name
		self.dicenum = dicenum
		self.dicesize = dicesize
		self.hpmod = hpmod
		self.desc = desc
		self.number = 0

	def addMob(self):
		self.number += 1
		a = 0 # rolling health
		for x in xrange(1,dicenum):
			a = a + random.randrange(1,dicesize)
		return Mob(self.name, a+hpmod, self.number)

class Mob(object):
	"""Mob: instance of Monster in a combat encounter"""
	def __init__(self, name, health, number):
		super(Mob, self).__init__()
		self.name = "%s %s" % (name, number)
		self.health = health
		self.maxHP = health
		self.statuses = []

						