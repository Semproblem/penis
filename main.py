n=int(input())
pervaya=0
for i in range(len(str(n))):
    s = str(n)
    jopas = int(s[i])
    if jopas%3==0 and jopas>pervaya:
        pervaya=jopas
if pervaya==0:
    print('NO')
else:
    print(pervaya)
