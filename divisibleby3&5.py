def fun(n):
  return n % 3 == 0 and n % 5 == 0

x = input("Enter the number: ")
x = int(x)
li = list(range(1, x)) 
print(list(filter (fun, li)))
