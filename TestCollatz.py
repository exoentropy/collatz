#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To test the program:
% python TestCollatz.py > TestCollatz.out
% chmod ugo+x TestCollatz.py
% TestCollatz.py > TestCollatz.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_single

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("1 10\n")
        p = collatz_read(r)
        (i, j) = p.next()
        self.assert_(i == 1)
        self.assert_(j == 10)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval((1, 10))
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval((100, 200))
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval((201, 210))
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval((900, 1000))
        self.assert_(v == 174)

    #edge case
    def test_eval_5 (self) :
        v = collatz_eval((1, 1))
        self.assert_(v == 1)

    #test inclusive range
    def test_eval_6 (self) :
        v = collatz_eval((5, 5))
        self.assert_(v == 6)
    
    #test inclusive range
    def test_eval_7 (self) :
        v = collatz_eval((4, 5))
        self.assert_(v == 6)

    #test inclusive range
    def test_eval_7 (self) :
        v = collatz_eval((3, 4))
        self.assert_(v == 8)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, (1, 10), 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # --------------
    # collatz_single
    # --------------
    
    #test empty cache
    def test_collatz_single1 (self) :
        number = 5
        cache = [-1, -1, -1, -1, -1, -1, -1, -1]
        v = collatz_single(number, cache)
        self.assert_(v == 6)

    #test cache check (note: wrong value used in cache to show that it was not computed by the function)
    def test_collatz_single2 (self) :
        number = 5
        cache = [-1, -1, -1, -1, -1, 8, -1, -1]
        v = collatz_single(number, cache)
        self.assert_(v == 8)

    #test empty cache
    def test_collatz_single3 (self) :
        number = 3
        cache = [-1, -1, -1, -1, -1, -1, -1, -1]
        v = collatz_single(number, cache)
        self.assert_(v == 8)

    #test cache check (note: wrong value used in cache to show that it was not computed by the function)
    def test_collatz_single4 (self) :
        number = 3
        cache = [-1, -1, -1, 5, -1, -1, -1, -1]
        v = collatz_single(number, cache)
        self.assert_(v == 5)
    
    #test empty cache
    def test_collatz_single5 (self) :
        number = 1
        cache = [-1, -1, -1, -1, -1, -1, -1, -1]
        v = collatz_single(number, cache)
        self.assert_(v == 1)

    #loop edge case: shouldn't access cache because it doesn't enter the loop
    def test_collatz_single6 (self) :
        number = 1
        cache = [-1, 5, -1, 5, -1, -1, -1, -1]
        v = collatz_single(number, cache)
        self.assert_(v == 1)

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
