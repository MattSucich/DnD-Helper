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

	def addMob(self, parent):
		self.number += 1
		a = 0 # rolling health
		for x in range(1,self.dicenum):
			a = a + random.randrange(1,self.dicesize)
		return Mob(self.name, a+self.hpmod, self.number, parent)

class Mob(object):
	"""Mob: instance of Monster in a combat encounter"""
	def __init__(self, name, health, number, parent):
		super(Mob, self).__init__()
		self.name = str("%s %s" % (name, number))
		self.health = health
		self.maxHP = health
		self.recharge = 1
		self.statuses = [0,0,0,0]
		self.parent = parent #to reference description

						