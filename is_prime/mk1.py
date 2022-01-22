from itertools import islice


def is_prime(n):
    if n < 2:
        return False

    if n in (2, 3):
        return True

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True


class primes:
    def __init__(self):
        # self.next 代表下一个素数
        # 未开始计算前初始为 1
        self.next = 1

    def __iter__(self):
        return self

    def __next__(self):
        # 从上一个素数之后开始寻找
        n = self.next + 1
        while True:
            # 测试每一个 n 是否素数
            # 如是则保存到 self.next 并返回
            # 否则继续测试下一个
            if is_prime(n):
                self.next = n
                return self.next
            else:
                n += 1


list(islice(primes(), 0, 100000))

