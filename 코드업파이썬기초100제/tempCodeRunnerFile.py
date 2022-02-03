date =  list(input().split('.'))
rev_date = date[::-1]

rev_date[0], rev_date[1] = rev_date[1], rev_date[0]

result = '-'.join(rev_date)


print(result)

