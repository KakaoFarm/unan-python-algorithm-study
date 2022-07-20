a, b = tuple(map(int, input().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print(gcd(a,b))


def lcm(a,b):
    return int(gcd(a,b) * (a / gcd(a,b)) * (b/gcd(a,b)))


print(lcm(a,b))