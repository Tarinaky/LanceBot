#!/usr/bin/env python2.7
# coding=utf8
"""
Implementation of DMBot style dice specification language and math parser.
"""
from __future__ import unicode_literals
from __future__ import print_function

from parsley import *
import random


grammar = makeGrammar("""

Digit = :x ?(x in '0123456789') -> x
Integer = <Digit+>:x -> int(x)
Decimal = (Integer:i '.' Integer:f -> float("%d.%d" % (i,f))) | (Integer:i -> int(i))
SIForm = Decimal:a 'e' Decimal:b -> a * 10**b
Number = SIForm | Decimal | ('-' SIForm:x -> -1*x) | ('-' Decimal:x -> -1*x)
Letter = :x ?(x in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY') -> x


Dice = (Integer:a 'd' Integer:b <Letter*>:mod -> ('d'+mod, a, b)) | ('d' Integer:a <Letter*>:mod -> ('d'+mod, 1, a))
Terminal = Dice | Number

Paren = ('(' ws Expression:a ws ')' ws -> a) | Terminal

Division = (Paren:a ws '/' ws Division:b -> ('/', a, b)) | Paren
Multiplication = (Division:a ws '*' ws Multiplication:b -> ('*', a, b)) | Division

Addition = (Multiplication:a ws '+' ws Addition:b -> ('+', a, b)) | Multiplication
Subtraction = (Addition:a ws '-' ws Subtraction:b -> ('-', a, b)) | Addition
Subexpression = Subtraction
Series = Subexpression:a ws ',' ws Subexpression:b -> (',', a, b)
Expression = Series | Subexpression

""", {})

def roll_dice(num, size):
    return [ random.randint(1,size) for _ in range(num) ]


def node_type(tree):
    (a,_,_) = tree
    return a


def evaluate_dice(tree):
    (_, left, right) = tree
    left = evaluate_tree(left)
    right = evaluate_tree(right)
    dice = roll_dice(left, right)
    return sum(dice)
    
eval_bindings = {
        'd': evaluate_dice
}
        

def make_tree(string):
    return grammar(string).Expression()

def evaluate_tree(tree):
    if isinstance(tree, int) or isinstance(tree, float):
        return tree
    if isinstance(tree, tuple):
        return eval_bindings[node_type(tree)](tree)

class Dice(object):
    def __init__(self, string):
        make_tree


    @property
    def roll(self):
        return self.tree


