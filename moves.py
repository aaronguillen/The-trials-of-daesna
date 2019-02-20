#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 16:22:51 2019

@author: chuckdye
"""
#move potion and spell list as class.
#list of possible moves with damage output followed by hit% as a decimal 
class Attack:
    def __init__(self,name, damage, hitchance):
        self.name = name
        self.damage = damage
        self.hitchance = hitchance
swing = Attack('Swing Sword', 8, 0.7)
thrust = Attack('Thrust Sword', 10, 0.6)
