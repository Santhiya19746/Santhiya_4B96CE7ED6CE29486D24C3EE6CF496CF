# function to find n' th fibonacci number
def factorial(n):
  return 1 if (n < 1) else n * factorial(n - 1)


if __name__ == '__main__':

  n = 6
print(f'the factorial of {n} is', factorial(n))
