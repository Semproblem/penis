n=int(input())
pervaya=0
for i in range(len(str(n))):
    s = str(n)
    currenDigit = int(s[i])
    if currenDigit%3==0 and currenDigit>pervaya:
        pervaya=currenDigit
if pervaya==0:
    print('NO')
else:
    print(pervaya)
