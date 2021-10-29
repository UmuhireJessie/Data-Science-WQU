# # Problem 1
# 
# Compute the five smallest positive even numbers.  Provide these in a list.

# # SOLUTION

even_numbers = [n for n in range(11) if n%2 == 0 and n != 0]
print(even_numbers)



# # Problem 2
# 
# Define a function that accepts a list (called `numbers` below) as input and return a list where each element is multiplied by 10.
# The grader will supply the argument `numbers` to the function when you run the `grader.score.in__problem2` method below.
# 
## SOLUTION

def mult(numbers):
    return [int(n)*10 for n in numbers]

test_numbers = [1, 2, 3]

mult(test_numbers)

