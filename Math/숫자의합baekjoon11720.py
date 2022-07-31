def main():
    n = int(input())
    word = input()
    result = 0
    for i in word:
        result += int(i)
    return result

print(main())