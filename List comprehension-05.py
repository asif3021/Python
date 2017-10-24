vec=[[1,2,3],[4,5,6],[7,8,9]]
new=[]
for element in vec:
    for n in element:
        #if n is vec
        #print(n,end=",")
        new.append(n)

print(new)


vec=[[1,2,3],[4,5,6],[7,8,9]]
new2=[]

[new2.append(num) for element in vec for num in element]
print(new2)
