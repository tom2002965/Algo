# from audioop import reverse
def permute(values):
    n = len(values)
    
    for i in reversed(range(n - 1)):
        if values[i] < values[i+1]:
            break
        
    else:
        values[:] = reversed(values[:])
        
        return values
    
    for j in reversed(range(i, n)):
        if values[i] < values[j]:
            values[i], values[j] = values[j], values[i]
            values[i+1 : ] = reversed(values[i+1:])
            break
        
    return values


print permute(list('42531'))

# print reversed('3')