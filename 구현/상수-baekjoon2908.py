import sys
'''
numbers = list( sys.stdin.readline().rstrip().split())

reversed_numbers = list()
for num in numbers:
    num = num[::-1]
    reversed_numbers.append(num)

print(max(reversed_numbers))
'''


def main():
    num_reversed = reversed_numbers()
    greater_reversed_number = max(num_reversed)

    return greater_reversed_number


def reversed_numbers():
    numbers = list(sys.stdin.readline().rstrip().split())
    num_reversed = list()
    for num in numbers:
        num = num[::-1]
        num_reversed.append(num)

    return num_reversed


print(main())







