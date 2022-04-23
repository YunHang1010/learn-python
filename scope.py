def increase_one(n):
    n += 1
    return n

n = 1
print(increase_one(n))
print(n)


def ressign(l):
    l = [0,1,2,3]
    
def append(l):
    l.append(3)
    
def modify(l):
    l[1] = 100

l = [0,1,2]
ressign(l)
print(l)
append(l)
print(l)
modify(l)
print(l)


