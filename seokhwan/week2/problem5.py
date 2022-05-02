def solution(phone_book):
  phone_book.sort(key=len)
  for i in range(len(phone_book)) :
    for j in range(i+1, len(phone_book)) :
      if phone_book[j].find(phone_book[i]) != -1 :
        return False
  return True
    
phone_book = input().split(" ")
print(solution(phone_book))