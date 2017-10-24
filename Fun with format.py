table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678131355256}
for name, phone in table.items():
    print('{0:10} ==> {1:13d}'.format(name, phone))




table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
