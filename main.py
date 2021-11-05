#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Function to take multiple arguments
from random import Random


class Dice :
    def role(self):
            ran = Random()
            first = ran.randint(1,6)
            second = ran.randint(1,6)
            return first,second

dice  = Dice()

print ("Dice > "+str(dice.role()))