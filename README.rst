Introduction
------------

This is an attempt to recreate a minimal subset of DMBot's functionality 
identically. This bot aims to support all previously valid DMBot dice and math
expressions while doing the minimal amount of development work.

Current Status
--------------
An off-the-shelf IRC Bot has been located and chosen. It has also been worked out
where in the existing code base (bot.py: dispatch) that our new math parser needs
to be 'plugged in'.

We are currently looking at Parsley as a way to build a new math parser, and
while it may not support the full range of DMBot's mathematical functions it should
be relatively easy to get it to support DMBot-style dice-specs as well as addition,
subtraction, multiplication and division. Watch this space.
