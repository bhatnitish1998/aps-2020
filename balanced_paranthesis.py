# Check whether the parenthesis are balanced or not

# Output : True if balanced else false

def areParanthesisBalanced(expr) : 
	stack = [] 
	for char in expr: 
		if char in ["(", "{", "["]: 
			stack.append(char) 
		else: 
			if not stack: 
				return False
			current_char = stack.pop() 
			if current_char == '(': 
				if char != ")": 
					return False
			if current_char == '{': 
				if char != "}": 
					return False
			if current_char == '[': 
				if char != "]": 
					return False
	if stack: 
		return False
	return True