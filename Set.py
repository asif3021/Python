y=[]
for x in 'abracadabra':
    if x not in set('abc'):
        y.append(x)

print(set(y))
