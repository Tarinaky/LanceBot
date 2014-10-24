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
Letter = :x ?(x in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY') -> x


Dice = (Integer:a 'd' Integer:b <Letter*>:mod -> ('d'+mod, a, b)) | ('d' Integer:a <Letter*>:mod -> ('d'+mod, 0, a))
Terminal = Dice | Number

Multiplication = Terminal:a ws '*' ws Term:b -> ('*', a, b)
Division = Terminal:a ws '/' ws Term:b -> ('/', a, b)
Term = Multiplication | Division | ('(' ws Expression:a ws ')' ws -> a) | Terminal

Addition = Term:a ws '+' ws Expression:b -> ('+', a, b)
Subtraction = Term:a ws '-' ws Expression:b -> ('-', a, b)
Expression = Series | Addition | Subtraction | Term
Series = Expression:a ws ',' ws Expression:b -> (',', a, b)

""", {})

class Dice(object):
    def __init__(self, string):
        self.tree = grammar(string).Expression()


    @property
    def roll(self):
        return self.tree


