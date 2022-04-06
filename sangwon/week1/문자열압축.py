from collections import deque
import copy

def solution(s):
    answer = 99999
    n=len(s)
    que=deque(list(s))
    tmp=copy.deepcopy(que)
    for i in range(1,n+1):
        total=0
        nowstr=''
        string=''
        for _ in range(i):
            nowstr+=que.popleft()
        arr=[[nowstr,1]]
        while len(que)>=i:
            string=''
            for _ in range(i):
                string+=que.popleft()
            if nowstr==string:
                arr[-1][1]+=1
            else:
                nowstr=string
                arr.append([nowstr,1])
        while que:
            string=que.popleft()
            arr.append([string,1])
            
        for e in arr:
            if e[1]==1:
                total+=len(e[0])
            else:
                total+=len(e[0])+len(str(e[1]))
        que=copy.deepcopy(tmp)
        answer=min(answer,total)

    return answer