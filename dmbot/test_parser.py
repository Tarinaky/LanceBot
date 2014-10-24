#!/usr/bin/env python2.7
# coding=utf8

import parser

from unittest import TestCase

class TestParser(TestCase):

    def test_tree(self):
        tree = parser.make_tree("1")
        assert tree == 1, tree
        return

    def test_dice_float(self):
        tree = parser.make_tree("0.3")
        assert tree == 0.3, tree

        return

    def test_dice_siform(self):
        tree = parser.make_tree("7e6")
        assert tree == 7e6, tree
        return

    def test_dice_negative(self):
        tree = parser.make_tree("-7")
        assert tree == -7, tree
        return

    def test_dice_d20(self):
        tree = parser.make_tree("d20")
        assert tree == ('d', 1, 20), tree
        return

    def test_dice_d6(self):
        tree = parser.make_tree("d6")
        assert tree == ('d', 1, 6), tree
        return

    def test_simple_math_add_mult(self):
        tree = parser.make_tree("3+1*2")
        assert tree == ('+', 3, ('*', 1, 2)), tree
        return

    def test_simple_math_sub_div(self):
        tree = parser.make_tree("2+6/3")
        assert tree == ('+', 2, ('/', 6, 3)), tree
        return

    def test_simple_math_mult_div(self):
        tree = parser.make_tree("10/2*5")
        assert tree == ('*', ('/', 10, 2), 5), tree
        return

    def test_modifier(self):
        tree = parser.make_tree("d10 + 12 - 2")
        assert tree == ('-', ('+', ('d', 1, 10), 12), 2), tree
        return 

    def test_group(self):
        tree = parser.make_tree("3d6")
        assert tree == ('d', 3, 6), tree
        return

    def test_series(self):
        tree = parser.make_tree("d6,6")
        assert tree == (',', ('d', 1, 6), 6), tree
        return

    def test_series_modifier(self):
        tree = parser.make_tree("d6+2,6")
        assert tree == (',', ('+', ('d', 1,6),2),6), tree
        return

    def test_dnd_chargen(self):
        tree = parser.make_tree("4d6l,6")
        assert tree == (',', ('dl', 4, 6), 6), tree
        return

    def test_shadowrun(self):
        tree = parser.make_tree("d6f,1000")
        assert tree == (',', ('df', 1, 6), 1000)
        return

    def test_brackets(self):
        tree = parser.make_tree("(1+2)*2")
        assert tree == ('*', ('+', 1, 2), 2)
        return
