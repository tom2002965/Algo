from collections import Counter

def find_min(freq):
    item = min(freq, key=lambda i: i[0])
    freq.remove(item)
    return item

def print_codes(tree, prefix=''):
    if isinstance(tree, tuple):
        print_codes(tree[0], prefix + '0')
        print_codes(tree[1], prefix + '1')
    else:
        print(tree, prefix)
        
def huffman_codes(text):
    freq = [(i, x) for x, i in Counter(text).items()]
    
    while len(freq) > 1:
        li, lx = find_min(freq)
        ri, rx = find_min(freq)
        freq.append((li + ri, (lx, rx)))
    
    print_codes(freq.pop()[1])
    
print huffman_codes('astala vista tasta')