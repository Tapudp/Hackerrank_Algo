#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    aliceScore, bobScore = 0, 0
    
    alice = [a0, a1, a2]
    bob = [b0, b1, b2]

    
    for i in range(3):
        if(alice[i] > bob[i]):
            aliceScore += 1
        elif(alice[i] == bob[i]):
            aliceScore += 0
            bobScore += 0
        else:
            bobScore += 1
    return [aliceScore, bobScore]
""" 
    if(a0 > b0):
        aliceScore += 1
    #elif(a0 == b0):
        #aliceScore = aliceScore
        if (a1>b1):
            aliceScore += 1
        #elif(a1 == b1):
            #aliceScore = aliceScore
            if(a2>b2):
                aliceScore += 1
            #elif(a2 == b2):
             #   aliceScore = aliceScore
            else:
                bobScore += 1
        else:
            bobScore += 1
    else:
        bobScore += 1
    if (a0 == b0 and a1 == b1 and a2 == b2):
        aliceScore += 0
        bobScore += 0
    return [aliceScore, bobScore]
"""
a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))


