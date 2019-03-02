"""
Problem:
    Alice and Bob each created one problem for HackerRank.
    A reviewer rates the two challenges, awarding points 
    on a scale from  to  for three categories: problem 
    clarity, originality, and difficulty.

    We define the rating for Alice's challenge to be the 
    triplet a = (a[0], a[1], a[2]), and the rating for 
    Bob's challenge to be the triplet b = (b[0], b[1], b[2]).

    Your task is to find their comparison points by 
    comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

    If a[i] > b[i], then Alice is awarded  point.
    If a[i] < b[i], then Bob is awarded  point.
    If a[i] = b[i], then neither person receives a point.
    Comparison points is the total points a person earned.

    Given a and b, determine their respective comparison points.

    For example, a = [1, 2, 3] and b=[3, 2, 1]. For elements 0, 
    Bob is awarded a point because a[0] < b[0]. For the equal 
    elements a[1] and b[1], no points are earned. Finally, 
    for elements 2, a[2] > b[2] so Alice receives a point. 
    Your return array would be [1, 1] with Alice's score first and 
    Bob's second.


>>> compare_the_triplets((3, 2, 1), (1, 2, 3))
[1, 1]

>>> compare_the_triplets((3, 3, 3), (1, 1, 1))
[3, 0]

>>> compare_the_triplets((1, 1, 1), (3, 3, 3))
[0, 3]

>>> compare_the_triplets((1, 1, 1), (1, 1, 1))
[0, 0]
"""

def compare_the_triplets(a, b):
    result = [0, 0]
    i = 0

    while i < 3:
        if a[i] > b[i]:
            result[0] += 1
        elif a[i] < b[i]:
            result[1] += 1
        
        i += 1
        
    return result