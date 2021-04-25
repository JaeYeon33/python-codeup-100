# 첫 번째 줄에 합
# 두 번째 줄에 차,
# 세 번째 줄에 곱,
# 네 번째 줄에 몫,
# 다섯 번째 줄에 나머지,
# 여섯 번째 줄에 나눈 값을 순서대로 출력한다.
# (실수, 소수점 이하 둘째 자리까지의 정확도로 출력)

import sys


def num_sum(n1, n2):
    return n1 + n2


def num_minus(n1, n2):
    return n1 - n2


def num_mul(n1, n2):
    return n1 * n2


def num_mok(n1, n2):
    return n1 // n2


def num_nameoji(n1, n2):
    return n1 % n2


def num_namum_gab(n1, n2):
    return round(n1 / n2, 2)


a, b = map(int, sys.stdin.readline().split())

print(num_sum(a, b))
print(num_minus(a, b))
print(num_mul(a, b))
print(num_mok(a, b))
print(num_nameoji(a, b))
print(num_namum_gab(a, b))
