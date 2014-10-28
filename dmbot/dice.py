#!/usr/bin/env python2.7
# coding=utf8
"""
Class-based wrapper around dmbot parser
"""
from __future__ import unicode_literals
from __future__ import print_function

from parser import *

class Dice(object):
    def __init__(self, string="0"):
        self.tree = 0
        self.set_string(string)
        return

    def set_string(self, string):
        self._string = string
        self.tree = make_tree(string)
        return self

    @property
    def string(self):
        return self._string

    @property
    def roll(self):
        return evaluate_tree(self.tree)

