# The nubmer which is occuring only once while others occur in pairs

#I nput: List of numbers

# Output: Returns the number which is occuring only once


def lonelyinteger(a):
    res=0
    for i in a:
        res=res^i
    return res