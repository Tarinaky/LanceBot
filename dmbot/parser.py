#!/usr/bin/env python2.7
# coding=utf8
"""
Implementation of DMBot style dice specification language and math parser.
"""
from __future__ import unicode_literals
from __future__ import print_function

from parsley import *

grammar = makeGrammar("""

Digit = :x ?(x in '0123456789') -> x
Integer = <Digit+>:x -> x
Decimal = (Integer:i '.' Integer:f -> float("%s.%s" % (i,f))) | (Integer:i -> int(i))
SIForm = Decimal:a 'e' Decimal:b -> a * 10**b
Number = SIForm | Decimal | ('-' SIForm:x -> -1*x) | ('-' Decimal:x -> -1*x)


Dice = (Integer:a 'd' Integer:b -> ('d', a, b)) | ('d' Integer:a -> ('d', 0, a))
Terminal = Dice | Number

Multiplication = Terminal:a ws '*' ws Term:b -> ('*', a, b)
Division = Terminal:a ws '/' ws Term:b -> ('/', a, b)
Term = Multiplication | Division | ('(' ws Expression:a ws ')' ws -> a) | Terminal

Addition = Term:a ws '+' ws Expression:b -> ('+', a, b)
Subtraction = Term:a ws '-' ws Expression:b -> ('-', a, b)
Expression = Addition | Subtraction | Term

""", {})

class Dice(object):
    def __init__(self, string):
        self.tree = grammar(string).Expression()


    @property
    def roll(self):
        return self.tree


