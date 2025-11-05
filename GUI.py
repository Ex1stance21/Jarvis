a = ['j', 'a', 'r', 'v', 'i', 's']
b = ['j', 'o', 'r', 'v', 'i', 's']
g = 0
for i in a:
    for e in b:
        if e == i:
            g = len(e)
print(g)