n = int(input())
i = 1
val = 0
while i <= n:
  if n%i == 0:
     val += 1
  i += 1
if val == 2:
  print("prime")
else :
  print("composite")