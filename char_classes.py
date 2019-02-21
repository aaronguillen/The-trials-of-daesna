# Trials of Desna Character Classes
# Created 2019-02-20
# Last Updated 2019-02-20
# Python 3.7.2
# -*- encoding: utf-8 -*-
# @author chuckdye and aaronguillen

class Character:
	"""Base class for all characters"""
	
	def __init__(self, name = "Unnamed Character"):
		self.name = name
		self.set_rand_stats()
	
	def set_rand_stats(self):
		def get_rand_stat_value():
			from random import randint
			
			# We're recreating the roll of 4 dice
			numdice = 4
			
			# A list to collect the outcome of our rolls
			addends = []
			for i in range(0, numdice):
				# "Roll the dice"
				# 1 - 6 because we're rolling d6's
				addends.append(randint(1, 6))
			
			sum = 0
			for i in sorted(addends)[1:numdice]:
				sum += i
			
			return sum
		
		self.str = get_rand_stat_value()
		self.con = get_rand_stat_value()
		self.dex = get_rand_stat_value()
		self.wis = get_rand_stat_value()
		self.int = get_rand_stat_value()
		self.cha = get_rand_stat_value()
		
	def reroll_stats(self):
		self.set_rand_stats()
	
	def print_stats(self):
		print("Str = ", self.str)
		print("Con = ", self.con)
		print("Dex = ", self.dex)
		print("Int = ", self.int)
		print("Wis = ", self.wis)
		print("Cha = ", self.cha)
		
class PlayerCharacter(Character):
	pass