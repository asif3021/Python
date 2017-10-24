def fun(*arg,**key):
    for ar in arg:
        print(ar)
    print(80*"-")
    for ky in key:
        print(ky,":",key[ky])



# test data
# fun("asif","ahmed","rishat",Name="Asif Ahmed",Id="1234",Varsity="DIU")
