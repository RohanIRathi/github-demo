# Add Implementation
def add(x,y):
	return x+y

# Subtract implementation
def subtract(x,y):
	return x-y # On master branch

# Multiply implementation
def multiply(x,y):
	return x*y # On bug0004 branch

# Divide Implementation
def divide(x,y):
	if x<0: # On master branch
		return "Error: Negative Parameter"
	if y == 0: # On bug0005 branch
		return "Error: Cannot divide by 0"
	else:
		return x/y

def square(x):
    return x**2