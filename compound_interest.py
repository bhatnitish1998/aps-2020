# Compound interest

def compound_interest(principle, rate, time): 
	CI = principle * (pow((1 + rate / 100), time)) 
	return(CI)
