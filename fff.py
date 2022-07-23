from functools import lru_cache
def hod(h):
    return h+2,h*2,h*3
@lru_cache(None)
def f(h):
    if (h>95 and h%2==0):
        return 'END'
    elif ( any(f(x)=='END' for x in hod(h))):
        return 'S1'
    elif ( all(f(x)=='S1' for x in hod(h))):
        return 'F1'
    elif ( any(f(x)=='F1' for x in hod(h))):
        return 'S2'
    elif ( all(f(x)=='S2' or f(x)=='S1' for x in hod(h))):
        return 'F2'
k=0
for i in range(1,30):
    try:
        k=f(i)
    except RecursionError:
        print('-')
    print(i, k)
    
    
