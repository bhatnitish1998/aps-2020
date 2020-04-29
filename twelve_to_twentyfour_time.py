# convert a string representing time in 12 hour format to 24 hour format

# Input : 12 hour time string in format "HH:MM:SS:XM"

# Returns a string representing time in 24 hour format as "HH:MM:SS"

def timeConversion(s):
    if s[-2]=='A':
        if s=="12:00:00AM":
            return "00:00:00"
        elif s[0]=='1' and s[1]=='2':
            return("00"+s[2:-2])
        else:
            return(s[0:-2])
    else:
        if s=="12:00:00PM":
            return "12:00:00"
        elif s[0]=='1' and s[1]=='2':
            return(s[0:-2])
        else:
            a=int(s[0:2])
            a=a+12
            return(str(a)+s[2:-2])
            
