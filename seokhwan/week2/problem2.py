testCount = int(input())

output = []
for i in range(testCount) :
  inputs = input().split(" ")
  
  allSum = 0
  for j in range(int(inputs[0])) :
    allSum += int(inputs[j+1])
  avg = allSum/int(inputs[0])
  
  count = 0
  for j in range(int(inputs[0])) :
    if avg < int(inputs[j+1]) :
      count += 1
  
  output.append((count/int(inputs[0]))*100)

for i in output :
  print("{:.3f}%".format(i))