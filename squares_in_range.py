# Number of squares in a given range

# Input: Two integers left and right limit both inclusibe

# Output: Number of squares in the givne range

def squares(a, b):
    value=0
    x=math.sqrt(a)
    y=math.sqrt(b)
    if x.is_integer():
        value+=1
    if y.is_integer():
        value+=1
    x=math.floor(x)
    y=math.ceil(y)
    value+=int(y-x-1)
    return(value)