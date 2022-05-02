inputStr = input()

num1 = int(inputStr.split(" ")[0])
num2 = int(inputStr.split(" ")[1])

sangso_num1 = (num1%10) * 100 + int(num1/10)%10 * 10 + int(num1/100)
sangso_num2 = (num2%10) * 100 + int(num2/10)%10 * 10 + int(num2/100)

if sangso_num1 > sangso_num2 :
  print(sangso_num1)
elif sangso_num1 < sangso_num2 :
  print(sangso_num2)