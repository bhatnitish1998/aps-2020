# Flip the bits in a 32 bit integer

# Input :Integer

# Output: Number representing input with  its bits flipped

def flippingBits(n):
    a=int('11111111111111111111111111111111',2)
    return n^a