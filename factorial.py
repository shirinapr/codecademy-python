def factorial(x):
  for i in range(1,x):
    x*=i
  return x

print(factorial(5))