#It can be seen that the number, 
# 125874, 
# and its double, 
# 251748, 
# contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.


# smallest int is a helpful clue, start low go high
# first thought is a simple ascending search, we can probably think about the starting point and some blacklisting of numbers
# second thought is we do some combinational checking.  Not sure what this would look like exactly, 

# I like the idea of starting with the 6x and checking if it's dividing values have the same digits.  Why is this helpful? Helpful because we can consider values only which evenly divide into 2,3,4,5
# 36
# 30
# 24
# 18
# 12
#  6

# but no, that's exactly the same as shifting along by one for x.  Anyway

from typing import Callable
from math import ceil


def containSameDigits(a:int,b:int) -> bool:
    """
    Docstring for containSameDigits
    
    :param a: integer for comparsion
    :type a: int
    :param b: other intiger for comparison
    :type b: int
    :return: True if a and b contain exactly the same characters
    :rtype: bool
    """
    sA: str = str(a)
    sB: str = str(b)

    if len(sA) != len(sB) : 
        return False
    
    # safe for dupes because ensured same length
    for char in sA:
        if char not in sB:
            return False
    
    return True

def getMultiples(i:int) -> list:
    """
    gets the multiples of the input for [1..6]
    
    """
    return [e*i for e in [1,2,3,4,5,6]]

def main():
    def associativeAll(values:list[int],func:Callable[[int,int],bool]) -> bool:
        """
        Applies func to pairwise to elements in values. [0,1], [0,2], ... [0,n].
        
        :param values: a list of values 
        :type values: list
        :param func: Description
        :type func: Callable[[int,int],bool]
        :return: whether all calls of func return true
        :rtype: bool
        """

        # Basically an all but the function is invoked on pairs.  The technical term for this is associativity IIRC.  Basically, f( f(x,y) , z) === f( x , f(y,z) ) 
        for  elem in values[1:]:
            if not func(values[0],elem):
                return False

        return True
    
    # let's consider our bounds for the loop
    # So the trick here is considering the max value we can have before we ought to skip forward to the next batch.  
    # ie, what is the max value for a power of ten such that 6* does not spill over into the next power of ten?
    # another way of thinking about this is that len(x) must equal len(6x).  What's the largest value for this?
    # dumb way of solving: 1000 / 6 = 166.6, so floor that is 166.  So for a power of ten, we only need consider values < 5/3 of it


    powerOfTen:int = 3
    while True:
        for candidate in range(10**powerOfTen, ceil((10**powerOfTen)*(5/3.0))):
            if associativeAll(getMultiples(candidate),containSameDigits):
                print(candidate)
                return
        powerOfTen += 1
    


if __name__ == "__main__": 
    main()