# Authors: Aaron Elam, Zohair Khan, Mateo Escamilla, Ciana Pike
# F1 - Optional Project
# MATH 2472
# 12/04/2020
#
# This program uses Taylor polynomials
# to estimate values of the base-e exponential, sine,
# and cosine functions for inputs in the interval [−5, 5].
# The calculator allows the user to select a function
# (either <<<<e^x, sin x, or cos x>>>>> and a real value of x from
# the interval [−5, 5], and should return the correct value
# of the function at the selected value of x, accurate to at least eight decimal places.

# Remember to Google what you wanna do. If you can do it in C++, you can do it in Python.
# and remember, indentation really matters in Python!

import math   # only used for in errorChecker()

validFunctionList = ["e^x", "cos(x)", "sin(x)"]

# Finished function for finding factorial of a value
def factorial(n):
  # base case
    if n == 0:
        return 1
    else:
      # recursively multiply n and previous factorial
        return n * factorial(n - 1)

# Function for calculating Taylor series approximation of a given function
def taylor(function, x):
  sum = 0
  allowedError = 0.00000001
  # Note: '**' denotes exponential in Python
  if(function == 'sin(x)'):
    n = 6   #TODO: programatically find n
    for k in range(n):
      sum += (-1)**k * ((x**((2*k)+1))/factorial((2*k)+1))
    return sum
  if(function == 'cos(x)'):
    n = 6
    for k in range(n):
      sum += ((-1)**k / factorial(2*k)) * x**(2*k)
    return sum
  if(function == 'e^x'):
    n = 8
    for k in range(n):
      sum += x**k/factorial(k)
    return sum
  

# Finished function to check error of our approximation
# Accuracy needs to be within 0.00000001 (7 zeroes or 1*10^-8)
def errorChecker(function, x, myApprox):
  if(function == 'sin(x)'):
    realValue = math.sin(x)               # does sine
  if(function == 'cos(x)'):
    realValue = math.cos(x)               # does cosine
  if(function == 'e^x'):
    realValue = math.exp(x)
  errorValue = abs(realValue - myApprox)  # take absolute value of difference
  #return errorValue

  # Ensure accuracy is appropriate
  allowedError = 0.00000001
  if errorValue < allowedError:
    print(f"Accuracy is within our bounds of {allowedError:.8f}")
  else:
    print(f"Accuracy is NOT within our bounds of {allowedError:.8f}")

  print(f"Accuracy of Taylor sim for {function}: {errorValue:.11f}") # :.9f will force non-sci notation


def main():
    # This while true loop will ask for function, then x until user enters both correctly.
    while True:
      try:
        function = input("Enter the function you want: (e^x, cos(x), sin(x)): ")
        if function in validFunctionList:
          ## Ask user for float in range [-5,5]
          user_x = int(input(f"Enter the x you want to use in {function} (in range [-5,5]): "))
          if -5 <= user_x <= 5:
            break # leave while True loop bc function and x are valid
          print("Enter a valid x between -5 and 5 inclusive.\n")
        print("Enter a valid function such as 'e^x', 'cos(x)', or 'sin(x)' exactly as printed.\n")
      except Exception as e:  # just in case there's a major messup
        print(e)
    # end while true loop

    # Calculate Taylor series approximation
    myApprox = taylor(function, user_x)

    print(f"Value of {function} where x = {user_x} is: {myApprox}")

    # Check error of our Taylor series approximation
    errorChecker(function, user_x, myApprox)


# weird python stuff we gotta have
if __name__ == "__main__":
    main()
