#!/usr/bin/env python2.7
# coding=utf8

import parser

from unittest import TestCase

class TestParser(TestCase):

    def test_dice_constructor(self):
        dice = parser.Dice("1").roll
        assert dice == 1, "Value was %d" % dice
        return

    def test_dice_float(self):
        dice = parser.Dice("0.3").roll
        assert dice == 0.3, "Value was %d" % dice
        return

    def test_dice_siform(self):
        dice = parser.Dice("7e6").roll
        assert dice == 7e6
        return

    def test_dice_negative(self):
        dice = parser.Dice("-7").roll
        assert dice == -7
        return

    def test_dice_d20(self):
        dice = parser.Dice("d20").roll
        assert dice <= 20
        assert dice >= 1
        return

    def test_dice_d6(self):
        dice = parser.Dice("d6").roll
        assert dice <= 6
        assert dice >= 1
        return

    def test_simple_math_add_mult(self):
        dice = parser.Dice("3+1*2").roll
        assert dice == 5
        return

    def test_simple_math_sub_div(self):
        dice = parser.Dice("2+6/3").roll
        assert dice == 5
        return

    def test_simple_math_mult_div(self):
        dice = parser.Dice("10/2*5").roll
        assert dice == 25
        return

    def test_modifier(self):
        dice = parser.Dice("d10 + 12 - 2").roll
        assert dice >= 11
        assert dice <= 20
        return 

    def test_group(self):
        dice = parser.Dice("3d6").roll
        assert dice >= 3
        assert dice <= 18
        return

    def test_series(self):
        dice = parser.Dice("d6,6").roll
        assert dice.size == 6
        for die in dice:
            assert die <= 6
            assert die >= 1
        return

    def test_series_modifier(self):
        dice = parser.Dice("d6+2,6").roll
        assert dice.size == 6
        for die in dice:
            assert die >= 3
            assert die <= 8
        return

    def test_dnd_chargen(self):
        dice = parser.Dice("4d6l,6").roll
        assert dice.size == 6
        for die in dice:
            assert die <= 18
            assert die >= 3
        return

    def test_shadowrun(self):
        dice = parser.Dice("d6f,1000").roll
        assert dice.size == 1000
        for die in dice:
            assert die >= 1
            assert (die % 6) != 0
        return


