#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2013
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
	r is a reader
	returns an generator that iterates over a sequence of lists of ints of length 2
	for s in r :
	l = s.split()
	b = int(l[0])
	e = int(l[1])
	yield [b, e]
	"""
    return (map(int, s.split()) for s in r)

# ------------
# collatz_eval
# ------------

def collatz_eval ((i, j)) :
    """
	i is the beginning of the range, inclusive
	j is the end of the range, inclusive
	return the max cycle length in the range [i, j]
	"""
    #error checking; switch i and j if range is invalid
    if (i > j):
        iTemp = i
        i = j
        j = iTemp
    #-1 implies that cache has not been written to for this number
    cache = [-1] * 1000000
    #Quiz 3 optimization
    m = j / 2
    if (i < m):
        i = m
    maxCycleLength = 1
    cacheAccess = 0
    cacheWrite = 0
    print (i, j)
    for number in range(i, j):

        if (cache[number] == -1):
            numberCycleLength = collatz_single(number, cache)
            cache[number] = numberCycleLength
            cacheWrite += 1
        
        if (cache[number] >= 1):
            numberCycleLength = cache[number]
            cacheAccess += 1

        if (numberCycleLength > maxCycleLength):
            maxCycleLength = numberCycleLength
        
    print ("cache accesses: ", cacheAccess)
    return maxCycleLength

# --------------
# collatz_single
# --------------
def collatz_single (number, cache):
	"""
	number is a single integer
	return the collatz solution for a single number (to help collatz_eval function)
	"""
	cycles = 0
        while (number > 1):
            if (cache[number] >= 1):
                return cache[number] + cycles
            cycles += 1
            if (number % 2 == 0):
                number = (3 * number) - 1
            else:
                number /= 2
        return cycles

	
# -------------
# collatz_print
# -------------

def collatz_print (w, (i, j), v) :
    """
	prints the values of i, j, and v
	w is a writer
	v is the max cycle length
	i is the beginning of the range, inclusive
	j is the end of the range, inclusive
	"""
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
	read, eval, print loop
	r is a reader
	w is a writer
	"""
    for t in collatz_read(r) :
        v = collatz_eval(t)
        collatz_print(w, t, v)
