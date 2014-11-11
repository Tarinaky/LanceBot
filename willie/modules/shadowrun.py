#coding=utf8
"""
shadowrun.py
Copyright 2014, Emma 'Tarinaky' Smith
Licensed under the Eiffel Forum License 2.


http://github.com/Tarinaky/LanceBot/
"""

from __future__ import unicode_literals

from willie.module import commands, rule, example, priority
from willie.tools import iterkeys

import re

from dmbot.dice import Dice

def count_successes(dice, tn):
    dice =  [ 1 if die >= tn else 0 for die in dice ]
    return sum(dice)

def find_largest(dice):
    largest = 0
    for die in dice:
        largest = die if (die > largest) else largest
    return largest

@commands('sr')
@example(r'!sr <dice> [<target number> [<repeats>]]')
def sr3_dice_roll(bot, trigger):
    """
    Shadowrun Third Edition Dice roller, supporting hidden Target Numbers 
    (1 argument supplied), open Target Numbers (two arguments supplied) and batch
    rolling (three arguments supplied).
    """

    trigger = re.search(r'(\d+)(?: +(\d+)(?: +(\d+))?)?(?: *:(.*))?', trigger)

    dice = trigger.group(1)
    tn = trigger.group(2)
    repeats = trigger.group(3)
    comment = trigger.group(4)
    calculate_sux = True
    display_comment = "'%s' " % comment

    if comment is None:
        display_comment = ""
    if tn is None:
        calculate_sux = False
        tn = 4
    else:
        tn = int(tn)
    if repeats is None:
        repeats = 1
    else:
        repeats = int(repeats)
    results = [ Dice("d6f,%s" % (dice) ).roll for _ in range(repeats) ]
    successes = [ count_successes(dice, tn) for dice in results ]
    open_test = [ find_largest(dice) for dice in results ]
        
    if repeats > 1:
        bot.reply("%sOpen Tests: %s or Success Tests: %s" % (display_comment, str(open_test), str(successes) ) )
    elif calculate_sux:
        bot.reply("%s%s = %s sux" % (display_comment, str(results[0]), str(successes[0]) ) )
    else:
        bot.reply("%s%s"%(display_comment, str(results[0]) ) )








