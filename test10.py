# -*- coding: utf-8 -*-

# [B반][게임공학과][2009182022][류웅국]
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = r"Im \\\ a \\\ cat.\n"
lazy_cat = r"I'am \\ a \\ lazy\\ cat."

fat_cat = '''
    I'll do a list:
    \t* Cat food
    \t* Fishies
    \t* Catnip\n\t* Grass
    '''

print tabby_cat
print persian_cat
print "%r"%backslash_cat
print fat_cat
print "%r" %lazy_cat
print  fat_cat
