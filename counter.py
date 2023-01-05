# Write your function below!
def fizz_count(x):
  count=0
  for item in x:
    if item=='fizz':
      count+=1
  return count

print(fizz_count(["fizz","fizz","fizz"]))
