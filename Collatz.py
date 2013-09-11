#!/usr/bin/env python

import sys

def collatz_read (r) :
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
    #-1 implies that cache has not been written to for this number
    cache = [-1] * 1000000
    #error checking; switch i and j if range is invalid
    if (i > j):
        iTemp = i
        i = j
        j = iTemp
    #Quiz 3 optimization
    m = j / 2
    if (i < m):
        i = m
    maxCycleLength = 1
    for number in range(i, j + 1):
        if (number < len(cache) and cache[number] != -1):
            numberCycleLength = cache[number]
        else:
            cacheTrace = [-1] * 600
            numberCycleLength = collatz_single(number, cache, cacheTrace)
            if(numberCycleLength < len(cacheTrace) - 1):
                collatz_cache_trace(numberCycleLength, cache, cacheTrace)
            if (number < len(cache)):
                cache[number] = numberCycleLength
        if (numberCycleLength > maxCycleLength):
            maxCycleLength = numberCycleLength
    return maxCycleLength



# --------------
# collatz_single

# --------------
def collatz_single (number, cache, cacheTrace):
    """
    number is from the collatz_eval loop
    evaluates the cylces for a single number
    """
    cycles = 1
    traceIndex = 0
    while (number > 1):
        if (number < len(cache) and cache[number] != -1):
            return cycles + cache[number] - 1
        cycles += 1
        if (number % 2 == 1):
            number = (3 * number) + 1
        else:
            number = (number / 2)
        if(cycles < len(cacheTrace) - 1):        
            cacheTrace[traceIndex] = number
        traceIndex += 1
    return cycles

# -------------------
# collatz_cache_trace
# -------------------
def collatz_cache_trace (numberCycleLength, cache, cacheTrace):
    newCycleLength = numberCycleLength - 1
    for traceIndex in range(0, numberCycleLength - 1):
        if(cacheTrace[traceIndex] < len(cache) and cache[cacheTrace[traceIndex]] == -1):
            cache[cacheTrace[traceIndex]] = newCycleLength
        newCycleLength -= 1

# -------------
# collatz_print
# -------------

def collatz_print (w, (i, j), v) :
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    for t in collatz_read(r) :
        v = collatz_eval(t)
        collatz_print(w, t, v)

collatz_solve(sys.stdin, sys.stdout)
