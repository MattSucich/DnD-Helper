import random

class Monster(object):
	"""Monster: stores name, description and hit dice for adding mobs to the combat order"""
	def __init__(self, dump):
		self.__dict__ = dump
	def __init__(self, name = "Undefined", dicenum = 1, dicesize = 1, hpmod = 1, desc = " "):
		super(Monster, self).__init__()
		self.name = name
		self.dicenum = dicenum
		self.dicesize = dicesize
		self.hpmod = hpmod
		self.desc = desc
		self.number = 0

	def edit(self, name = "Undefined", dicenum = 1, dicesize = 1, hpmod = 1, desc = " "):
		self.name = name
		self.dicenum = dicenum
		self.dicesize = dicesize
		self.hpmod = hpmod
		self.desc = desc

	def addMob(self, parent):
		self.number += 1
		a = 0 # rolling health
		for x in range(0,self.dicenum):
			try:
				a = a + random.randrange(1,self.dicesize)
			except:
				a = a + 1;
		return Mob(self.name, a+self.hpmod, self.number, parent)

class Mob(object):
	"""Mob: instance of Monster in a combat encounter"""
	def __init__(self, dump):
		self.__dict__ = dump
	def __init__(self, name = "1", health = 1, number = 1, parent = 1):
		super(Mob, self).__init__()
		self.name = str("%s %s" % (name, number))
		self.health = health
		self.maxHP = health
		self.recharge = 1
		self.statuses = [0] * 13
		self.parent = parent #to reference description

						