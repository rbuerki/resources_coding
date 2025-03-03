# Uses python3
import sys
from typing import List


def max_dot_product(a: List[int], b: List[int]) -> int:
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    # write your code here
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = list(map(int, input().split()))
    n = data[0]
    a = data[1 : (n + 1)]
    b = data[(n + 1) :]
    print(max_dot_product(a, b))
