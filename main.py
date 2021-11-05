#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Function to take multiple arguments
from random import Random


class Coin:
    def flip(self):
        random  = Random()
        face  = {
            1:"Head",
            2:"Tail"
        }
        num = random.randint(1,2)
        return  face.get(num)

coin  = Coin()
print (coin.flip())