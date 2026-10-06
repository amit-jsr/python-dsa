"""Problem 36

Write a `@retry(times=3)` decorator for a function that sometimes raises an
exception.

Example:
Input:  @retry(times=3) on a function that fails twice, then succeeds
Output: returns the result on the 3rd attempt

Input:  same function failing every time
Output: raises the last exception after 3 attempts
"""


# Write your solution below

def retry(times=3):
    pass
