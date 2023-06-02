def FirstFactorial(num):
  factorial = 1

  if num<1:
    return "there's no factorial"
  elif num == 0:
    factorial = 0
  else:
    for i in range ( 1, num + 1):
      factorial = factorial*i

  # code goes here
  return factorial

# keep this function call here 
print(FirstFactorial(3))
