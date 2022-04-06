from collections import deque

def solution(new_id):
    ans = deque([])
    for c in new_id:
        if c.isalpha(): 
            ans.append(c.lower())
        elif c.isdecimal() or c == '-' or c == '_' or c == '.':
            ans.append(c)
            if len(ans)>=2:
                if ans[-1]=='.' and ans[-2]=='.': 
                    ans.pop()
                    
    if ans and ans[0]=='.': 
        ans.popleft()
    if ans and ans[-1]=='.': 
        ans.pop()
    if not ans: 
        ans.append('a')
    if len(ans)>=16:
        while len(ans)>15:
            ans.pop()
        if ans[-1]=='.': 
            ans.pop()
    if len(ans)<=2:
        while len(ans)<3:
            ans.append(ans[-1])
    answer=''.join(map(str,ans))
    return answer