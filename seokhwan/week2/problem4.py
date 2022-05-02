def solution(participant, completion):
    for i in completion :
      participant.remove(i)
    return participant[0]

participant = input().split(" ")
completion = input().split(" ")

print(solution(participant, completion))