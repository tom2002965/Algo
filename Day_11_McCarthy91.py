def mccarthy91(n):
    k = 1
    while k :
        if n > 100:
            n -= 10
            k -= 1
        else:
            n += 11
            k += 1
    return n

def mccarthy91_rec(n):
    if n > 100:
        return n - 10
    else:
        return mccarthy91_rec(mccarthy91_rec(n + 11))
    
print mccarthy91(80)
print mccarthy91_rec(80)
        