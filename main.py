#!/usr/bin/env python
# -*- coding: utf-8 -*-




class Mammal:
    def __init__(self):
        pass
    def talk(self):
      print ("talk")


class Cat(Mammal):
    def __init__(self):
        pass


class Dog(Mammal):
    def __init__(self):
        pass

dog  = Dog()
dog.talk()