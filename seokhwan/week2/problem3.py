inputStr = input().upper()

charNum = {}
for i in inputStr :
  if i in charNum :
    charNum[i] += 1
  else :
    charNum[i] = 1

maxNum = 0
maxChar = ''
for i in charNum :
  if maxNum < charNum[i] :
    maxNum = charNum[i]
    maxChar = i
  elif maxNum == charNum[i] :
    maxNum = charNum[i]
    maxChar = '?'

print(maxChar)