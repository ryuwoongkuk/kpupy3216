# -*- coding: utf-8 -*-

# [B반][게임공학과][2009182022][류웅국]
age = raw_input("How old are you? ") #print 안하고 바로 출력하면서 input입력받아서 대입.
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
                                                    age, height, weight)