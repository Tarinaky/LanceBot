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
    dice = trigger.group(3)
    tn = trigger.group(4)
    repeats = trigger.group(5)
    calculate_sux = True

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
        bot.reply("Open Tests: %s; Success Tests: %s" % (str(open_test), str(successes) ) )
    elif calculate_sux:
        bot.reply("%s = %s sux" % (str(results[0]), str(successes[0]) ) )
    else:
        bot.reply(str(results[0]))








