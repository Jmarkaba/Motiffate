## AUTHOR: JAH MARKABAWI
## DATE: 07/19/2019
##
## Brute-force algorithm for finding repeating
## patterns in a list

def findPatterns(a, min_length=2, min_count=2, ):
    ## 
    # Find Patterns in Iterable
    # @params
    # a - list/tuple or string
    # Optional: 
    # min_length - minimum length of pattern
    # min_count - minimum occurrences of pattern
    # @returns 
    # dict of tuples or strings
    ##
    if type(a) == str:
        return _findRepeatsforString(a, min_length, min_count)
    elif type(a) == list or type(a) == tuple:
        return _findRepeatsForList(a, min_length, min_count)
    else:
        raise AssertionError("The input is neither a list nor a string")

def _list_count(lst, sub):
    cnt, size = 0, len(lst)
    for k in range(size):
        if lst[k] == sub[0]:
            eq = True
            for i, other in enumerate(sub):
                z = k+i
                if z >= size or lst[z] != other:
                    eq = False
                    break
            if eq: cnt += 1
    return cnt

def _findRepeatsForList(lst,MINLEN,MINCNT):
    d={}
    for sublen in range(MINLEN,int(len(lst)/MINCNT)):
        for i in range(0,len(lst)-sublen):
            sub = tuple(lst[i:i+sublen])
            cnt = _list_count(lst, sub)
            if cnt >= MINCNT and sub not in d:
                d[sub] = cnt
    return d

def _findRepeatsforString(s,MINLEN,MINCNT):
    d={}
    for sublen in range(MINLEN,int(len(s)/MINCNT)):
        for i in range(0,len(s)-sublen):
            sub = s[i:i+sublen]
            cnt = s.count(sub)
            if cnt >= MINCNT and sub not in d:
                d[sub] = cnt
    return d

if __name__ == '__main__':
    print(findPatterns([1,2,3,4,2,3,4,5,2,2,2,2,1,2,3]))
    print(findPatterns([1,2,3,4,2,3,4,5,2,2,2,2,1,2,3],2,3))