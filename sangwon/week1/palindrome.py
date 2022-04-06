from bwsi_grader.python.palindrome import grader

def student_func(x):
    arr = []
    x = x.lower()
    length = len(x)
    l = 0
    r = length-1

    flag = True
    while (l<=r and r>=0 and l<length):
        if x[l] == " ": 
            l+=1
            continue
        if x[r] == " ":
            r-=1
            continue
        if (x[l] != x[r]):
            flag = False
            break
        l+=1
        r-=1
    return flag

grader(student_func)