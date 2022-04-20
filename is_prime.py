from math import sqrt
from itertools import islice


def is_prime(n):
    if n<=1:
        return False
    if n in (2,3):
        return True
    for i in range(2,int(sqrt(n) + 1)):
        if n%i == 0:
            return False
    return True

def prime(n):
    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield n
        else:
            continue

def prime_numbers(n):
    return list(islice(prime(n),0,n))

if __name__ == '__main__':
    while True:
        try:
            n = int(input('你想输出前几位素数，请输入此时此刻数字：'))
            break
        except ValueError:
            print('不是整数，请重新输入')
        
    print(f"前{n}位素数是",prime_numbers(n))